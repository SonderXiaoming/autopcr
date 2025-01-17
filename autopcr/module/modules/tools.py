from typing import List

from ...db.models import GachaExchangeLineup
from ...model.custom import GachaReward
from ..modulebase import *
from ..config import *
from ...core.pcrclient import pcrclient
from ...model.error import *
from ...db.database import db
from ...model.enums import *
import datetime

@description('来发十连，或者直到出货')
@name('抽卡')
@singlechoice("pool_id", "池子", db.get_cur_gacha()[0], db.get_cur_gacha())
@booltype("cc_until_get", "抽到出", False)
@default(True)
class gacha_start(Module):
    def can_stop(self, new, exchange: List[GachaExchangeLineup]):
        r = set(item.unit_id for item in exchange)
        return any(item.id in r for item in new)

    async def do_task(self, client: pcrclient):
        gacha_id = int(self.get_config('pool_id').split(':')[0])
        resp = await client.get_gacha_index()
        for gacha in resp.gacha_info:
            if gacha.id == gacha_id:
                target_gacha = gacha
                break
        else:
            raise AbortError(f"未找到卡池{gacha_id}")
        if target_gacha.type != eGachaType.Payment:
            raise AbortError("非宝石抽卡池")

        reward = GachaReward()
        always = self.get_config('cc_until_get')
        cnt = 0
        try:
            while True:
                cnt += 1
                reward += await client.exec_gacha_aware(target_gacha, 10, eGachaDrawType.Payment, client.data.jewel.free_jewel + client.data.jewel.jewel, 0)
                if not always or self.can_stop(reward.new_unit, db.gacha_exchange_chara[target_gacha.exchange_id]) :
                    break
        except:
            raise 
        finally:
            self._log(f"抽取了{cnt}次十连")
            self._log(await client.serlize_gacha_reward(reward))
            self._log(f"当前pt为{client.data.gacha_point[target_gacha.exchange_id].current_point}")

@description('获得可导入到兰德索尔图书馆的账号数据')
@name('兰德索尔图书馆导入数据')
@default(True)
class get_library_import_data(Module):
    async def do_task(self, client: pcrclient):
        msg = client.data.get_library_import_data()
        self._log(msg)

@description('根据每个角色拉满星级、开专、升级至当前最高专所需的记忆碎片减去库存的结果')
@booltype("sweep_get_able_unit_memory", "地图可刷取角色", False)
@name('获取记忆碎片缺口')
@default(True)
class get_need_memory(Module):
    async def do_task(self, client: pcrclient):
        demand = list(client.data.get_memory_demand_gap().items())
        demand = sorted(demand, key=lambda x: x[1], reverse=True)
        if self.get_config("sweep_get_able_unit_memory"):
            demand = [i for i in demand if i[0] in db.memory_quest]

        msg = '\n'.join([f'{db.get_inventory_name_san(item[0])}: {"缺少" if item[1] > 0 else "盈余"}{abs(item[1])}片' for item in demand])
        self._log(msg)

@description('根据每个角色开专、升级至当前最高专所需的心碎减去库存的结果，大心转换成10心碎')
@name('获取心碎缺口')
@default(True)
class get_need_xinsui(Module):
    async def do_task(self, client: pcrclient):
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
        msg = '\n'.join(msg)
        self._log(msg)

@inttype("start_rank", "起始品级", 1, [i for i in range(1, 99)])
@booltype("like_unit_only", "收藏角色", False)
@description('统计指定角色拉满品级所需的装备减去库存的结果，不考虑仓库中的大件装备')
@name('获取装备缺口')
@default(True)
class get_need_equip(Module):
    async def do_task(self, client: pcrclient):
        start_rank: int = self.get_config("start_rank")
        like_unit_only: bool = self.get_config("like_unit_only")

        demand = list(client.data.get_equip_demand_gap(start_rank=start_rank, like_unit_only=like_unit_only).items())

        demand = sorted(demand, key=lambda x: x[1], reverse=True)

        msg = '\n'.join([f'{db.get_inventory_name_san(item[0])}: {"缺少" if item[1] > 0 else "盈余"}{abs(item[1])}片' for item in demand])
        self._log(msg)

@inttype("start_rank", "起始品级", 1, [i for i in range(1, 99)])
@booltype("like_unit_only", "收藏角色", False)
@description('根据装备缺口计算刷图优先级，越前的优先度越高')
@name('刷图推荐')
@default(True)
class get_normal_quest_recommand(Module):
    async def do_task(self, client: pcrclient):
        start_rank: int = self.get_config("start_rank")
        like_unit_only: bool = self.get_config("like_unit_only")

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

        msg = '\n--------\n'.join(tot)
        self._log(msg)
