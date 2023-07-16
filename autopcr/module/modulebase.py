from ..model.common import ItemType
from ..core.pcrclient import pcrclient
from typing import DefaultDict, List, Dict, Tuple, Iterator, Union
from collections import defaultdict
from abc import abstractmethod
from ..model.error import *
from ..db.database import db
from ..model.enums import *
import datetime

def _wrap_init(cls, setter):
    old = cls.__init__
    def __init__(self, *args, **kwargs):
        old(self, *args, **kwargs)
        setter(self)
    cls.__init__ = __init__
    return cls

def default(val):
    return lambda cls:_wrap_init(cls, lambda self: setattr(self, '_val', val))
def description(desc: str):
    return lambda cls:_wrap_init(cls, lambda self: setattr(self, 'description', desc))
def enumtype(candidates: list):
    def wrapper(cls):
        cls = _wrap_init(cls, lambda self: (setattr(self, 'type', 'enum'), setattr(self, 'candidates', candidates)))
        old = cls.do_task
        async def do_task(self, client: pcrclient):
            if self.value is None or self.value == "none":
                raise SkipError('功能未启用')
            elif self.value not in self.candidates: 
                raise ValueError(f"未知的选项{self.value}")
            else: 
                return await old(self, client)
        cls.do_task = do_task
        return cls

    return wrapper
def booltype(cls):
    cls = _wrap_init(cls, lambda self: (setattr(self, 'type', 'bool'), setattr(self, 'candidates', [True, False])))
    old = cls.do_task
    async def do_task(self, client: pcrclient):
        if self.value: 
            return await old(self, client)
        else: 
            raise SkipError('功能未启用')
    cls.do_task = do_task
    return cls
def notimplemented(cls):
    return _wrap_init(cls, lambda self: setattr(self, 'implmented', False))

# refers to a schudule to be done
class Module:
    def __init__(self, parent: "ModuleManager"):
        self._val: Union[str, int, bool, None] = None
        self.candidates: list = []
        self.name: str = self.__class__.__name__
        self.description: str = self.name
        self.type = 'invalid'
        self.implmented = True
        self._parent = parent
        self.log = []
    @property
    def value(self):
        return self._val
    @value.setter
    def value(self, val):
        try:
            iv = int(val)
            if iv in self.candidates: val = iv
        except:
            pass
        if val in self.candidates:
            msg = f'{self.name}: {self._val} => {val}'
            self._val = val
            return msg
        else:
            return self.candidates[0]
            # raise AbortError(f"Invalid value for module {self.name}")

    @abstractmethod
    async def do_task(self, client: pcrclient): ...

    def cron_hook(self) -> int:
        return None

    def get_config(self, name):
        return self._parent.get_config(name)
    def generate_config(self):
        return {
            'value': self.value,
            'description': self.description,
            'candidates': self.candidates,
            'type': self.type,
            'candidate_value': self.candidates,
            'implemented': self.implmented
        }

    def _log(self, msg):
        self.log.append(msg)

import json
import traceback
class ModuleManager:
    _modules: List[type] = []

    def __init__(self, filename):
        self._filename = filename
        self.modules: Dict[str, Module] = {clazz.__name__: clazz(self) for clazz in self._modules}
        self._crons = []
        self._load_config()
    
    def _load_config(self):
        try:
            with open(self._filename, 'r') as f:
                self.data = json.load(f)
            self._load_from(self.data)
        except:
            traceback.print_exc()
            raise
            # self.data = {'username': '', 'password': '', 'alian': '', 'qq': ''}
    
    def _load_from(self, data):
        self._crons.clear()
        for name, module in self.modules.items():
            if name in data:
                module.value = data[name]
                self.data[name] = data[name]
            cron = module.cron_hook()
            if cron: self._crons.append(cron)
        # 这里对time1和time2进行兼容
        if data.get('time1open', False): self._crons.append(int(data['time1'].split(':')[0]))
        if data.get('time2open', False): self._crons.append(int(data['time2'].split(':')[0]))
    
    def save_config(self):
        data = {m.name: m.value for m in self.modules.values()}
        for k, v in data.items():
            self.data[k] = v
        with open(self._filename, 'w') as f:
            json.dump(self.data, f)
    
    def get_config(self, name):
        return self.modules[name].value
    
    def update_config(self, data):
        self._load_from(data)

    def generate_config(self):
        return {
            # 'username': self.data['username'],
            # 'password': self.data['password'],
            'alian': self.data['alian'],
            'qq': "",
            'username': "",
            'password': "",
            'time1': self.data.get("time1", False),
            'time2': self.data.get("time2", False),
            'time1open': self.data.get('time1open', "00:00"),
            'time2open': self.data.get('time2open', "00:00"),
            'data': [{'name': m.name, 'value': m.generate_config()} for m in self.modules.values()],
            'last_result': self.data.get('_last_result', None)
        }
    
    async def do_cron(self, hour):
        if hour in self._crons:
            await self.do_task()

    def get_ios_client(self) -> pcrclient: # Header TODO
        client = pcrclient({
            'account': self.data['username'],
            'password': self.data['password'],
            'channel': 1000,
            'platform': 1
        })
        return client

    def get_android_client(self) -> pcrclient:
        client = pcrclient({
            'account': self.data['username'],
            'password': self.data['password'],
            'channel': 1,
            'platform': 2
        })
        return client

    async def get_library_import_data(self):
        try:
            client = self.get_android_client()
            await client.login()
            msg = client.data.get_library_import_data()
            return msg
        except Exception as e:
            traceback.print_exc()
            raise(e)

    async def get_normal_quest_recommand(self, start_rank: int, like_unit_only: bool) -> List[str]:
        try:
            client = self.get_android_client()
            await client.login()
            quest_list: List[int] = [id for id, quest in db.normal_quest_data.items() if db.parse_time(quest.start_time) <= datetime.datetime.now()]
            require_equip = client.data.get_equip_demand_gap(start_rank = start_rank, like_unit_only = like_unit_only)
            quest_weight = client.data.get_quest_weght(require_equip)
            quest_id = sorted(quest_list, key = lambda x: quest_weight[x], reverse = True)
            tot = []
            for i in range(10):
                id = quest_id[i]
                name = db.quest_name[id]
                tokens: List[ItemType] = [i for i in db.normal_quest_rewards[id]]
                msg = f"{name}:\n" + '\n'.join([
                    (f'{db.get_inventory_name_san(token)}: {"缺少" if require_equip[token] > 0 else "盈余"}{abs(require_equip[token])}片')
                    for token in tokens])
                tot.append(msg.strip())

            return tot
        except Exception as e:
            traceback.print_exc()
            raise(e)

    async def get_need_equip(self, start_rank: int, like_unit_only: bool):
        try:
            client = self.get_android_client()
            await client.login()
            demand = list(client.data.get_equip_demand_gap(start_rank, like_unit_only).items())

            demand = sorted(demand, key=lambda x: x[1], reverse=True)

            title = [f'{db.get_inventory_name_san(item[0])}: {"缺少" if item[1] > 0 else "盈余"}{abs(item[1])}片' for item in demand]
            return title
            # return title + msg
        except Exception as e:
            traceback.print_exc()
            raise(e)

    async def get_need_xinsui(self):
        try:
            client = self.get_android_client()
            await client.login()
            result, need = client.data.get_suixin_demand()
            result = sorted(result, key=lambda x: x[1])
            msg = [f"{db.get_inventory_name_san(item[0])}: 需要{item[1]}片" for item in result]

            store = client.data.get_inventory(db.xinsui) + client.data.get_inventory(db.heart) * 10
            cnt = need - store
            tot = f"当前心碎数量为{store}(大心自动转换成10心碎)，需要{need}，"
            if cnt > 0:
                tot += f"缺口数量为:{cnt}"
            elif cnt < 0:
                tot += f"盈余数量为:{-cnt}"
            else:
                tot += "当前心碎储备刚刚好！"
            msg = [tot] + msg
            return msg
        except Exception as e:
            traceback.print_exc()
            raise(e)

    async def get_need_memory(self):
        try:
            client = self.get_android_client()
            await client.login()
            demand = list(client.data.get_memory_demand_gap().items())
            demand = sorted(demand, key=lambda x: x[1])

            msg = [f'{db.get_inventory_name_san(item[0])}: {"缺少" if item[1] > 0 else "盈余"}{abs(item[1])}片' for item in demand]
            return msg
        except Exception as e:
            traceback.print_exc()
            raise(e)

    async def do_task(self):
        result: Dict[int, Dict[str, str]] = {}
        try:
            client = self.get_android_client()
            await client.login()
            cnt = 0
            client.keys['_last_clean_time'] = self.data['_last_clean_time'] if '_last_clean_time' in self.data else None
            for name in (x.__name__ for x in ModuleManager._modules):
                module = self.modules[name]
                result[cnt] = {"name": name, "value": module.value if module.type != "bool" else "", "desc": module.description, "msg": "", "status": ""}
                try:
                    module.log.clear()
                    await module.do_task(client)
                    result[cnt]["msg"] = ""
                    result[cnt]["status"] = "success"
                except SkipError as e:
                    result[cnt]["msg"] = str(e)
                    result[cnt]["status"] = "skip"
                except AbortError as e:
                    result[cnt]["msg"] = str(e)
                    result[cnt]["status"] = "abort"
                except Exception as e:
                    traceback.print_exc()
                    result[cnt]["msg"] = str(e)
                    result[cnt]["status"] = "error"
                finally:
                    result[cnt]['msg'] = ('\n'.join(module.log) + "\n" + result[cnt]['msg']).strip() or "ok"
                cnt += 1
        except Exception as e:
            traceback.print_exc()
            raise(e)
        finally:
            self.data['_last_result'] = result
            self.data['_last_clean_time'] = db.format_time(datetime.datetime.now())
        return result
