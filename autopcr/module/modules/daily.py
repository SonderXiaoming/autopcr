from ..modulebase import *
from ..config import *
from ...core.pcrclient import pcrclient
from ...model.error import *
from ...db.database import db
from ...model.enums import *
import datetime

@description('赛马')
@default(True)
class chara_fortune(Module):
    async def do_task(self, client: pcrclient):
        if not db.is_cf_time():
            raise SkipError("今日无赛马")
        if client.data.cf is None:
            raise SkipError("今日已赛马")
        res = await client.draw_chara_fortune()
        self._log(f"赛马第{client.data.cf.rank}名，获得了宝石x{res.reward_list[0].received}")

@description('开始时领取任务奖励')
@default(True)
class mission_receive_first(Module):
    async def do_task(self, client: pcrclient):
        resp = await client.mission_index()
        for mission in resp.missions:
            if db.is_daily_mission(mission.mission_id) and mission.mission_status == eMissionStatusType.EnableReceive:
                resp = await client.mission_receive()
                reward = await client.serlize_reward(resp.rewards)
                self._log("领取了任务奖励，获得了:\n" + reward)
                return
        raise SkipError("没有可领取的任务奖励")

@description('结束时领取任务奖励')
@default(True)
class mission_receive_last(Module):
    async def do_task(self, client: pcrclient):
        resp = await client.mission_index()
        for mission in resp.missions:
            if db.is_daily_mission(mission.mission_id) and mission.mission_status == eMissionStatusType.EnableReceive:
                resp = await client.mission_receive()
                reward = await client.serlize_reward(resp.rewards)
                self._log("领取了任务奖励，获得了:\n" + reward)
                return
        raise SkipError("没有可领取的任务奖励")

@description('EXP探索')
@default(True)
class explore_exp(Module):
    async def do_task(self, client: pcrclient):
        exp_quest_remain = client.data.training_quest_max_count.exp_quest - client.data.training_quest_count.exp_quest
        if exp_quest_remain:
            quest_id = client.data.get_max_avaliable_quest_exp()
            if not quest_id:
                raise AbortError("不存在可扫荡的exp探索")
            name = db.quest_name[quest_id]
            await client.training_quest_skip(quest_id, exp_quest_remain)
            self._log(f"{name}扫荡{exp_quest_remain}次")
        else:
            raise SkipError("exp已扫荡")

@description('MANA探索')
@default(True)
class explore_mana(Module):
    async def do_task(self, client: pcrclient):
        gold_quest_remain = client.data.training_quest_max_count.gold_quest - client.data.training_quest_count.gold_quest
        if gold_quest_remain:
            quest_id = client.data.get_max_avaliable_quest_mana()
            if not quest_id:
                raise AbortError("不存在可扫荡的mana探索")
            name = db.quest_name[quest_id]
            await client.training_quest_skip(quest_id, gold_quest_remain)
            self._log(f"{name}扫荡{gold_quest_remain}次")
        else:
            raise SkipError("mana已扫荡")

@singlechoice("present_receive_strategy", "领取策略", "非体力", ["非体力", "全部"])
@description('领取礼物箱')
@default(True)
class present_receive(Module):
    async def do_task(self, client: pcrclient):
        if self.get_config('present_receive_strategy') == "非体力":
            is_exclude_stamina = True
            op = "领取了非体力物品：\n"
        else:
            is_exclude_stamina = False
            op = "领取了所有物品：\n"
        received = False
        result = []
        stop = False
        while not stop:
            present = await client.present_index()
            for present in present.present_info_list:
                if not is_exclude_stamina or not (present.reward_type == eInventoryType.Stamina and present.reward_id == 93001):
                    print(present.reward_type, present.reward_id)
                    res = await client.present_receive_all(is_exclude_stamina)
                    if not res.rewards:
                        stop = True
                    else:
                        result += res.rewards
                        received = True
                    break
            else:
                stop = True

        if not received:
            raise SkipError(f"不存在未领取{'的非体力的' if is_exclude_stamina == True else '的'}礼物")
        msg = await client.serlize_reward(result)
        self._log(op + msg)


@description('领取双场币')
@default(True)
class jjc_reward(Module):
    async def do_task(self, client: pcrclient):
        info = await client.get_arena_info()
        if info.reward_info.count:
            await client.receive_arena_reward()
        self._log(f"jjc币x{info.reward_info.count}")
        info = await client.get_grand_arena_info()
        if info.reward_info.count:
            await client.receive_grand_arena_reward()
        self._log(f"pjjc币x{info.reward_info.count}")

@description('基本信息')
@default(True)
class user_info(Module):
    async def do_task(self, client: pcrclient):
        now = db.format_time(datetime.datetime.now())
        self._log(f"{client.data.name} 体力{client.data.stamina}({db.team_max_stamina[client.data.team_level].max_stamina}) 等级{client.data.team_level} 钻石{client.data.jewel.free_jewel} mana{client.data.gold.gold_id_free} 扫荡券{client.data.get_inventory((eInventoryType.Item, 23001))} 母猪石{client.data.get_inventory((eInventoryType.Item, 90005))}\n清日常时间:{now}")


