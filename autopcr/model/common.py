#type: ignore
from typing import List
from .enums import *
from pydantic import BaseModel
from .common import eInventoryType

class AgreementStatus(BaseModel):
	ver: int = None
	state: int = None
class Alchemy(BaseModel):
	max_count: int = None
	exec_count: int = None
class ArenaCountInfo(BaseModel):
	battle_number: int = None
class ArenaInfo(BaseModel):
	max_battle_number: float = None
	battle_number: int = None
	interval_end_time: int = None
	yesterday_defend_number: int = None
	highest_rank: int = None
	season_highest_rank: int = None
	rank: int = None
	group: int = None
	group_moving_release_time: int = None
class ArenaSetting(BaseModel):
	time_reset_cost: int = None
	count_reset_cost: int = None
class BattleLogData(BaseModel):
	battle_log_type: int = None
	type: int = None
	target_unit_id: int = None
	target_is_own_unit: int = None
	source_unit_id: int = None
	source_is_own_unit: int = None
	action_id: int = None
	frame: int = None
	value1: int = None
	value2: int = None
	value3: int = None
	duration: int = None
	current_value: int = None
	wave_count: int = None
class BattleLogType(BaseModel):
	miss: int = None
	set_damage: int = None
	set_abnormal: int = None
	set_recovery: int = None
	set_buff_debuff: int = None
	set_state: int = None
	button_tap: int = None
	set_energy: int = None
	damage_charge: int = None
	give_value_additional: int = None
	give_value_multiply: int = None
	wave_end_hp: int = None
	wave_end_damage_amount: int = None
	_break: int = None
class BossHistory(BaseModel):
	id: int = None
	difficulty: int = None
	lap_num: int = None
	order_num: int = None
	clear_time: int = None
	attack_count: int = None
class BossInfo(BaseModel):
	order_num: int = None
	enemy_id: int = None
	max_hp: int = None
	current_hp: int = None
class BossRank(BaseModel):
	enemy_id: int = None
	rank: int = None
class BulkSkipSetting(BaseModel):
	default_skip_count: int = None
	max_skip_count: int = None
class CampaignDate(BaseModel):
	start_time: str = None
	end_time: str = None
class CampaignGachaInfo(BaseModel):
	campaign_id: int = None
	fg1_exec_cnt: int = None
	fg1_last_exec_time: int = None
	fg10_exec_cnt: int = None
	fg10_last_exec_time: int = None
class CampaignTarget(BaseModel):
	viewer_id: int = None
	target_flag: bool = None
class CartoonSetting(BaseModel):
	open_time_sp: int = None
	open_time_dmm: int = None
class ChangeRarityUnit(BaseModel):
	unit_id: int = None
	battle_rarity: int = None
class ChangeToMaterial(BaseModel):
	key: int = None
	val: int = None
class CharaExchangeTicketProductData(BaseModel):
	csv_data_id: str = None
	number_of_product_purchased: int = None
	start_time: int = None
	end_time: int = None
class CharaExchangeTicketReward(BaseModel):
	unit_id: int = None
	unit_rarity: int = None
	reward_type: eInventoryType = None
	reward_id: int = None
	reward_count: int = None
class ChatMessageInfo(BaseModel):
	viewer_id: int = None
	message_id: int = None
	message_type: eClanChatMessageType = None
	message: str = None
	create_time: int = None
	disp_minigame_button: eClanChatPlayButtonCondition = None
class ClanBattleData(BaseModel):
	now_open: int = None
	is_interval: int = None
	next_open_time: int = None
	mode_change_limit_time: int = None
	mode_change_limit_start_time: int = None
	mode_change_limit_remind_time: int = None
	is_extra_battle_cleared: int = None
class ClanBattleSetting(BaseModel):
	default_difficulty: int = None
	default_challenge_count: int = None
	clan_point_coefficient: int = None
	support_rental_cost_coefficient: int = None
	border_unit_level: int = None
	grace_time: int = None
	dispatch_count_bonus_limit: int = None
	dispatch_time_bonus_limit: int = None
	hp_recovery_time: int = None
	can_use_hp_border: int = None
	support_lv_band: int = None
	monster_detail_reload_interval: int = None
	mode_change_limit_hours: int = None
	mode_change_limit_start_hours: int = None
	mode_change_limit_remind_hours: int = None
	party_copy_open_time: int = None
class ClanBattleTopUserClanInformation(BaseModel):
	clan_name: str = None
	clan_role: int = None
class ClanPoint(BaseModel):
	before_point: int = None
	after_point: int = None
	before_count: int = None
	after_count: int = None
	cost_group_id: int = None
class ClanProfileCardClanInfo(BaseModel):
	clan_name: str = None
	clan_battle_id: int = None
	period: int = None
	rank: int = None
	grade_rank: int = None
	level: int = None
	member_num: int = None
	join_condition: int = None
	activity: int = None
	last_clan_battle_mode: int = None
	last_battle_joined: int = None
class ClanProfileCardDisplayStatus(BaseModel):
	level: bool = None
	member: bool = None
class ClanProfileCardSetting(BaseModel):
	unit_id: int = None
	skin: int = None
	background: int = None
	frame: int = None
	disp_status: ClanProfileCardDisplayStatus = None
	invite_comment: str = None
	comment: str = None
class ClanSetting(BaseModel):
	max_member_num: int = None
	max_leader_num: int = None
	max_sub_leader_num: int = None
	dispatch_interval: int = None
	chat_num_per_time: int = None
	chat_max_num: int = None
	chat_expire_sec: int = None
	chat_polling_time: int = None
	gold_unit_period: int = None
	gold_base: int = None
	gold_rate_power: float = None
	gold_per_dispatch_count: int = None
	rejoin_restriction_time: int = None
	like_reward: int = None
	daily_like_reward_limit: int = None
	be_liked_reward: int = None
	daily_be_liked_reward_limit: int = None
	equipment_request_interval: int = None
	search_clan_default_activity: int = None
	search_clan_default_join_condition: int = None
	search_clan_default_member_condition_range: int = None
	notify_support_gold_border: int = None
	clan_activity_max: int = None
	rental_cost_fixed_border_team_lv: int = None
	rental_cost_rate_per_team_lv: int = None
	rental_cost_fixed: int = None
class ClearedExQuestList(BaseModel):
	quest_id: int = None
	ex_cleared_time: int = None
class CounterStopCoinInfo(BaseModel):
	count: int = None
	max: int = None
class DamageHistory(BaseModel):
	viewer_id: int = None
	enemy_id: int = None
	name: str = None
	damage: int = None
	kill: int = None
	create_time: int = None
	history_id: int = None
	lap_num: int = None
	order_num: int = None
class DearPointInfo(BaseModel):
	chara_index: int = None
	dear_point: int = None
class DearStoryInfo(BaseModel):
	story_id: int = None
	is_choiced: int = None
class DeckData(BaseModel):
	deck_number: ePartyType = None
	unit_id1: int = None
	unit_id2: int = None
	unit_id3: int = None
	unit_id4: int = None
	unit_id5: int = None
class DeckListData(BaseModel):
	deck_number: int = None
	unit_list: List[int] = None
class DispatchUnitStatus(BaseModel):
	owner_viewer_id: int = None
	unit_id: int = None
	hp: int = None
class DungeonArea(BaseModel):
	dungeon_type: int = None
	dungeon_area_ids: List[int] = None
class DungeonBattleMission(BaseModel):
	mission_id: int = None
	condition_value: int = None
	is_complete: bool = None
class DungeonBattleStartUnit(BaseModel):
	owner_viewer_id: int = None
	unit_id: int = None
class DungeonSetting(BaseModel):
	support_rental_cost_coefficient: int = None
	border_unit_level: int = None
	support_lv_band: int = None
class DuplicateUnitInfo(BaseModel):
	unit_id: int = None
	rarity: int = None
	count: int = None
class EmblemData(BaseModel):
	emblem_id: int = None
	ex_value: int = None
class EnhanceRecipe(BaseModel):
	id: int = None
	type: int = None
	count: int = None
	current_count: int = None
class EquipDonate(BaseModel):
	equip_id: int = None
	num: int = None
	name: str = None
class EquipRequests(BaseModel):
	message_id: int = None
	equip_id: int = None
	request_num: int = None
	donation_num: int = None
	user_donation_num: int = None
	history: List[EquipDonate] = None
	is_finish_checked: int = None
	viewer_id: int = None
class EquipSlot(BaseModel):
	id: int = None
	is_slot: bool = None
	enhancement_level: int = None
	enhancement_pt: int = None
	rank: int = None
	status: int = None
class EquipSlotLight(BaseModel):
	is_slot: bool = None
	enhancement_pt: int = None
	rank: int = None
class EventBoxGachaHitRewardInfo(BaseModel):
	box_set_id: int = None
	hit_reward_count: int = None
class EventBoxGachaSet(BaseModel):
	box_set_id: int = None
	step: int = None
	reward_type: eInventoryType = None
	reward_id: int = None
	reward_count: int = None
	inbox_count: int = None
	remain_inbox_count: int = None
	reset_target: int = None
	disp_group: int = None
	odds_file: str = None
class EventEnemyDamageInfo(BaseModel):
	enemy_identify: int = None
	total_damage: int = None
class EventGachaInfo(BaseModel):
	gacha_step: int = None
	box_set_list: List[EventBoxGachaSet] = None
class EventHitTreasureInfo(BaseModel):
	enemy_identify: int = None
	hit_treasure_index_list: List[int] = None
class EventQuizInfo(BaseModel):
	quiz_id: int = None
	is_correct: int = None
class EventSpecialBattleExRankingInfo(BaseModel):
	rank: int = None
	appear_num: int = None
	total_attack_num: int = None
	total_attack_num_mode1: int = None
	total_attack_num_mode2: int = None
	total_attack_num_mode3: int = None
	new: int = None
class EventSpecialEnemyUnit(BaseModel):
	unit_id: int = None
	hp: int = None
	order: int = None
class EventStatus(BaseModel):
	event_type: int = None
	event_id: int = None
	period: int = None
class EventSubStoryInfo(BaseModel):
	sub_story_id: int = None
	status: eEventSubStoryStatus = None
class FriendSetting(BaseModel):
	limit_accept: int = None
	limit_request: int = None
	limit_pending: int = None
class FriendSupportUnitIniSetting(BaseModel):
	support_interval: int = None
	gold_unit_period: int = None
	gold_base: int = None
	gold_rate_power: float = None
	gold_per_support_count: int = None
	support_count_bonus_daily_limit: int = None
	support_count_bonus_limit: int = None
	support_time_bonus_limit: int = None
	limit_unit_level: int = None
	consume_gold_rate: int = None
	consume_gold_limit: int = None
	support_lv_band: int = None
class GachaBonusItem(BaseModel):
	target_unit_id: int = None
	reward_type: eInventoryType = None
	reward_id: int = None
	reward_count: int = None
class GachaPointInfo(BaseModel):
	exchange_id: int = None
	current_point: int = None
	max_point: int = None
class GachaPointReset(BaseModel):
	exchange_id: int = None
	lost_gacha_point: int = None
class GachaPrizeHistoryList(BaseModel):
	exec_count: int = None
	rarity: int = None
	exec_time: int = None
class GaugeInfo(BaseModel):
	start_level: int = None
	total: int = None
	unit_id: int = None
	chara_id: int = None
	current_level: int = None
class GrandArenaCountInfo(BaseModel):
	battle_number: int = None
class GrandArenaInfo(BaseModel):
	max_battle_number: int = None
	battle_number: int = None
	interval_end_time: int = None
	winning_number: int = None
	yesterday_defend_number: int = None
	highest_rank: int = None
	season_highest_rank: int = None
	rank: int = None
	group: int = None
	group_moving_release_time: int = None
class GrandArenaSetting(BaseModel):
	time_reset_cost: int = None
	count_reset_cost: int = None
class GrowthParameterList(BaseModel):
	unit_rarity: int = None
	unit_level: int = None
	skill_level: int = None
	promotion_level: int = None
	equipment1: int = None
	equipment2: int = None
	equipment3: int = None
	equipment4: int = None
	equipment5: int = None
	equipment6: int = None
	love_level: int = None
	growth_id_list: List[int] = None
	equip_slot: List[int] = None
class HatsuneEventBossEnemyInfo(BaseModel):
	boss_id: int = None
	enemy_identify: int = None
	hp: int = None
class HatsuneEventBossStatus(BaseModel):
	boss_id: int = None
	hp: int = None
	is_unlocked: int = None
	appear_num: int = None
	attack_num: int = None
	kill_num: int = None
	is_force_unlocked: int = None
	daily_kill_count: int = None
	oneblow_kill_count: int = None
	enemy_identify: int = None
class HatsuneEventStatus(BaseModel):
	event_type: int = None
	event_id: int = None
	period: int = None
class HatsuneEventStoryState(BaseModel):
	story_id: int = None
	is_unlocked: int = None
	is_readed: bool = None
class HatsuneSeriesInfo(BaseModel):
	event_id: int = None
	is_hard_quest_unlocked: bool = None
	bosses: List[HatsuneEventBossStatus] = None
class HatsuneUserEventQuest(BaseModel):
	quest_id: int = None
	clear_flag: int = None
	result_type: int = None
	is_unlocked: int = None
	limit_time: int = None
	wave_pattern_ids: List[int] = None
	daily_clear_count: int = None
	daily_recovery_count: int = None
class IniPair(BaseModel):
	key: int = None
	val: int = None
class InventoryInfoPost(BaseModel):
	id: int = None
	type: int = None
	count: int = None
class InventoryInfoShort(BaseModel):
	id: int = None
	stock: int = None
	create_time: int = None
class ItemInfo(BaseModel):
	item_id: int = None
	item_num: int = None
	current_num: int = None
class ItemListRequest(BaseModel):
	item_type: int = None
	item_id: int = None
	item_num: int = None
class KaiserBattleIniSetting(BaseModel):
	support_lv_band: int = None
	support_limit: int = None
	allowable_damage_coefficient: float = None
	allowable_enemy_point: int = None
	allowable_barrier_point: int = None
	remaining_count_max: int = None
class KaiserBattleSupportRental(BaseModel):
	support_num: int = None
	owner_viewer_id: int = None
	support_unit_id: int = None
class KaiserBossInfo(BaseModel):
	kaiser_boss_id: int = None
	progress: int = None
	condition_count: int = None
	current_hp: int = None
	kill_count: int = None
	mode: int = None
	enemy_point: int = None
	attack_count: int = None
class KmkKillList(BaseModel):
	low: int = None
	middle: int = None
	high: int = None
class LastFriendTime(BaseModel):
	accept: int = None
	pending: int = None
class LevelInfo(BaseModel):
	team: GaugeInfo = None
	unit: List[GaugeInfo] = None
	love: List[GaugeInfo] = None
class LimitedShop(BaseModel):
	system_id: int = None
	close_time: int = None
class LimitSetting(BaseModel):
	limit_equipment_num: int = None
	limit_gold: int = None
	limit_jewel: int = None
	limit_free_jewel: int = None
class LoadDeckData(BaseModel):
	deck_number: ePartyType = None
	unit_id1: int = None
	unit_id2: int = None
	unit_id3: int = None
	unit_id4: int = None
	unit_id5: int = None
	battle_rarity1: int = None
	battle_rarity2: int = None
	battle_rarity3: int = None
	battle_rarity4: int = None
	battle_rarity5: int = None
class LoginBonusData(BaseModel):
	campaign_id: int = None
	total_count: int = None
	count_num: int = None
	type: str = None
	reward_type: eInventoryType = None
	reward_id: int = None
	reward_count: int = None
	lottery_type: int = None
class LoginBonusList(BaseModel):
	first: List[LoginBonusData] = None
	normal: List[LoginBonusData] = None
	campaign: List[LoginBonusData] = None
	lottery: List[LoginBonusData] = None
	adv: List[LoginBonusData] = None
	countdown: List[LoginBonusData] = None
	birthday: List[LoginBonusData] = None
	story_read_process: List[LoginBonusData] = None
class MaintenanceStatus(BaseModel):
	_from: int = None
	to: int = None
	from_date_time: int = None
	to_date_time: int = None
class MaterialInfo(BaseModel):
	material_id: int = None
	consume_num: int = None
	possession_num: int = None
class MaterialParameter(BaseModel):
	material_id: int = None
	material_count: int = None
class MaxExecNumList(BaseModel):
	arena_limit: int = None
	convert_rupee_limit: int = None
	dungeon_limit: int = None
	special_quest_limit: int = None
	stamina_limit: int = None
class MessageIni(BaseModel):
	message_id: int = None
	message: str = None
class MissionNotice(BaseModel):
	mission_id: int = None
	count: int = None
	max_times: int = None
class MissionRequestFlag(BaseModel):
	quest_clear_rank: int = None
class MusicIdData(BaseModel):
	bgm_key: eBGMKey = None
	music_id: int = None
class MusicPurchasedData(BaseModel):
	music_id: int = None
	purchased_time: int = None
class MyLogEnemyData(BaseModel):
	enemy_id: int = None
	damage: int = None
class MyPage(BaseModel):
	type: int = None
	id: int = None
	music_id: int = None
	still_skin_id: int = None
class MyProfileCardDisplayStatus(BaseModel):
	viewer_id: bool = None
	level: bool = None
	power: bool = None
	clan_battle: bool = None
	arena: bool = None
	grand_arena: bool = None
	tower: bool = None
class MyProfileCardScore(BaseModel):
	clan_battle_id: int = None
	clan_battle_score: int = None
	arena_rank: int = None
	grand_arena_rank: int = None
	tower_cleared_floor_num: int = None
	tower_cleared_ex_quest_count: int = None
	clan_id: int = None
	emblem_id_list: List[int] = None
	last_clan_battle_mode: int = None
class MyProfileCardSetting(BaseModel):
	unit_id: int = None
	skin: int = None
	emblem_id: int = None
	background: int = None
	frame: int = None
	disp_status: MyProfileCardDisplayStatus = None
	comment: str = None
class NormalGachaTerm(BaseModel):
	time: str = None
class OthersClanInfo(BaseModel):
	message_id: int = None
	quest_id: int = None
	lobby_id: int = None
	level_limit: int = None
	create_time: int = None
	accept_quest_time: int = None
	member_count: int = None
class PartsInfo(BaseModel):
	parts_id: int = None
	hp: int = None
class PctBonusInfo(BaseModel):
	bonus_type: int = None
	bonus_count: int = None
	add_point: int = None
class PctCacaoInfo(BaseModel):
	cacao_id: int = None
	stock: int = None
class PctGradeInfo(BaseModel):
	grade_type: int = None
	grade_count: int = None
class PctUnitPointInfo(BaseModel):
	unit_id: int = None
	pct_point: int = None
class PkbCatalogBatter(BaseModel):
	batter_id: int = None
	batting_num: int = None
	hit_num: int = None
	status: int = None
class PkbCatalogPitcher(BaseModel):
	pitcher_id: int = None
	status: int = None
	unlocked_ball_type: List[int] = None
class PkbHighScoreInfo(BaseModel):
	normal: int = None
	hard: int = None
	very_hard: int = None
	extra: int = None
class PkbReadRankingInfo(BaseModel):
	category: int = None
	difficulty_level: int = None
class PkbReplay(BaseModel):
	pitcher: int = None
	batter: int = None
	seed: int = None
	batting_time: int = None
	batting_pos: List[float] = None
	gauge: int = None
	happen_triggers: List[int] = None
	adrenaline_count: int = None
class PostMultiUnlockRarity6Slot(BaseModel):
	slot_id: int = None
	current_unlock_level: int = None
	after_unlock_level: int = None
	current_material_num: int = None
class PracticeDeckData(BaseModel):
	deck_number: int = None
	deck_name: str = None
	unit_id1: int = None
	unit_id2: int = None
	unit_id3: int = None
	unit_id4: int = None
	unit_id5: int = None
	mask_bit_flag: int = None
class PresentHistoryInfo(BaseModel):
	present_id: int = None
	reward_type: eInventoryType = None
	reward_id: int = None
	reward_count: int = None
	message_id: int = None
	message_param_value1: int = None
	message_param_value2: int = None
	message_param_value3: int = None
	message_param_value4: int = None
	create_time: int = None
class PresentParameter(BaseModel):
	present_id: int = None
	reward_type: eInventoryType = None
	reward_id: int = None
	reward_count: int = None
	reward_rarity: int = None
	message_id: int = None
	message_param_value1: int = None
	message_param_value2: int = None
	message_param_value3: int = None
	message_param_value4: int = None
	reward_limit_flag: eRewardLimitType = None
	reward_limit_time: int = None
	create_time: int = None
class Price(BaseModel):
	currency_type: eInventoryType = None
	currency_id: int = None
	currency_num: int = None
class ProfileQuestInfo(BaseModel):
	normal_quest: List[int] = None
	hard_quest: List[int] = None
	very_hard_quest: List[int] = None
class ProfileUserInfo(BaseModel):
	viewer_id: int = None
	user_name: str = None
	user_comment: str = None
	team_level: int = None
	team_exp: int = None
	arena_rank: int = None
	arena_group: int = None
	arena_time: int = None
	grand_arena_rank: int = None
	grand_arena_group: int = None
	grand_arena_time: int = None
	open_story_num: int = None
	unit_num: int = None
	total_power: int = None
	tower_cleared_floor_num: int = None
	tower_cleared_ex_quest_count: int = None
	emblem: EmblemData = None
	last_login_time: int = None
	friend_num: int = None
class PurchasedTimesData(BaseModel):
	csv_data_id: str = None
	number_of_product_purchased: int = None
class QuestRecoverInfo(BaseModel):
	quest_id: int = None
	daily_recovery_count: int = None
class QuestSetting(BaseModel):
	recovery_time: int = None
	challenge_count_special_gold: int = None
	challenge_count_special_exp: int = None
class QuestSkipInfo(BaseModel):
	quest_id: int = None
	skip_count: int = None
class RaceLoginBonusInfo(BaseModel):
	fortune_id: int = None
	rank: int = None
	seed: int = None
	unit_list: List[int] = None
class RaceLoginBonusRewardList(BaseModel):
	type: int = None
	id: int = None
	received: int = None
class RankingGroupInfo(BaseModel):
	group_id: int = None
	is_destination: int = None
class RankResult(BaseModel):
	clan_battle_id: int = None
	period: int = None
	clan_rank: int = None
	rank_in_clan: int = None
	clan_battle_mode: int = None
	lap_num: int = None
	total_kill_count: int = None
	battle_joined: int = None
class RecommendUnit(BaseModel):
	unit_id: int = None
	display_order: int = None
	growth_id: int = None
class RecoverChallengeCountSetting(BaseModel):
	recovery: int = None
	recovery_max_count: int = None
	cost: List[int] = None
class RecoverStamina(BaseModel):
	count: int = None
	exec_count: int = None
	recovery: int = None
	cost: int = None
class RefundItem(BaseModel):
	item_id: int = None
	type: eItemType = None
	number: int = None
class ReleaseContentData(BaseModel):
	system_id: str = None
	deck_list: List[DeckData] = None
class RestChallengeInfo(BaseModel):
	dungeon_type: int = None
	count: int = None
	max_count: int = None
class ReturnFesInfo(BaseModel):
	end_time: int = None
	original_gacha_id: int = None
	gacha_point_info: GachaPointInfo = None
	supply_unit_id_list: List[int] = None
	can_campaign_gacha: int = None
class RoleInfo(BaseModel):
	viewer_id: int = None
	role_id: int = None
class RoomExtensionItem(BaseModel):
	serial_id: int = None
	room_item_id: int = None
	color_id: int = None
class RoomItemGetTime(BaseModel):
	room_item_id: int = None
	get_time: int = None
class RoomItemPosition(BaseModel):
	serial_id: int = None
	direction: int = None
	x: int = None
	y: int = None
class RoomItemPositionForMyset(BaseModel):
	room_item_id: int = None
	direction: int = None
	x: int = None
	y: int = None
class RoomSetting(BaseModel):
	extension_room_storage_cost: int = None
	extension_room_storage_num: int = None
	max_room_storage_num: int = None
	shortening_time: int = None
	use_jewel: int = None
	not_stock_term: int = None
	max_stock_count: int = None
class RoomTheme(BaseModel):
	floor_theme: int = None
	wall_theme: int = None
	background_theme: int = None
class RoomUserItem(BaseModel):
	serial_id: int = None
	room_item_id: int = None
	room_item_level: int = None
	room_item_skin_id: int = None
	level_up_end_time: int = None
	item_base_time: int = None
	item_count: int = None
class SearchUserInfo(BaseModel):
	viewer_id: int = None
	user_name: str = None
	user_comment: str = None
	team_level: int = None
	last_login_time: int = None
class SeasonPackRewardInfo(BaseModel):
	reward_type: int = None
	reward_id: int = None
	reward_count: int = None
class SendApi(BaseModel):
	notice: int = None
	home: int = None
class SendGiftData(BaseModel):
	item_id: int = None
	item_num: int = None
	current_item_num: int = None
class SerialCodeIniSetting(BaseModel):
	restrict_release_sec: int = None
class Shop(BaseModel):
	alchemy: Alchemy = None
	recover_stamina: RecoverStamina = None
class ShopBuyInfo(BaseModel):
	system_id: int = None
	slot_id: int = None
	current_currency_num: int = None
	number: int = None
class ShopItem(BaseModel):
	type: eInventoryType = None
	slot_id: int = None
	item_id: int = None
	num: int = None
	sold: int = None
	end_time: int = None
	price: Price = None
	exchange_count: int = None
	available_num: int = None
	price_group: int = None
	seq_id: int = None
	stock_count: int = None
	purchase_count: int = None
	renewal_time: int = None
	banner_type: eShopItemBannerType = None
	gojuon_order: int = None
class SkillLevelInfo(BaseModel):
	skill_id: int = None
	skill_level: int = None
	slot_number: int = None
class SkillLevelInfoLight(BaseModel):
	skill_level: int = None
class SkillLevelUpDetail(BaseModel):
	location: int = None
	step: int = None
	current_level: int = None
class SkillLimitCounter(BaseModel):
	skill_id: int = None
	counter: int = None
class SkinChangeSetting(BaseModel):
	open_time: int = None
class SkinData(BaseModel):
	icon_skin_id: int = None
	sd_skin_id: int = None
	still_skin_id: int = None
	motion_id: int = None
class SkinDataForRequest(BaseModel):
	unit_id: int = None
	icon_skin_id: int = None
	sd_skin_id: int = None
	still_skin_id: int = None
	motion_id: int = None
class SkipGoldRewardInfo(BaseModel):
	count: int = None
class SrtCatalogInfo(BaseModel):
	reading_id: int = None
	status: eSrtCatalogStatus = None
class SrtHighScoreInfo(BaseModel):
	normal: int = None
	hard: int = None
	extra: int = None
class StartDashFesInfo(BaseModel):
	end_time: int = None
	original_gacha_id: int = None
	sdfes_gacha_point_info: GachaPointInfo = None
	supply_unit_id_list: List[int] = None
	can_campaign_gacha: int = None
class StatusParam(BaseModel):
	hp: int = None
	atk: int = None
	_def: int = None
	magic_str: int = None
	magic_def: int = None
	physical_critical: int = None
	magic_critical: int = None
	wave_hp_recovery: int = None
	wave_energy_recovery: int = None
	hp_recovery_rate: int = None
	physical_penetrate: int = None
	magic_penetrate: int = None
	life_steal: int = None
	dodge: int = None
	energy_reduce_rate: int = None
	energy_recovery_rate: int = None
	accuracy: int = None
class StatusParamShort(BaseModel):
	hp: int = None
	atk: int = None
	_def: int = None
	matk: int = None
	mdef: int = None
	crt: int = None
	mcrt: int = None
	hrec: int = None
	erec: int = None
	hrec_rate: int = None
	pnt: int = None
	mpnt: int = None
	life_steal: int = None
	dodge: int = None
	erec_rate: int = None
	ered_rate: int = None
	accuracy: int = None
class StrCoinCost(BaseModel):
	idx: int = None
	cost: int = None
class StrJewelCost(BaseModel):
	idx: int = None
	cost: int = None
class SupportUnitSetting(BaseModel):
	unit_id: int = None
	position: int = None
	support_start_time: int = None
	friend_support_count: int = None
	general_support_count: int = None
	clan_support_count: int = None
	friend_support_reward: int = None
	support_type: int = None
class TicketGachaParameter(BaseModel):
	id: int = None
	start_time: int = None
	end_time: int = None
	ticket_id: int = None
	exec_times: int = None
	url_param: str = None
	is_chara_exchange_ticket: bool = None
class TowerQueryUnit(BaseModel):
	owner_viewer_id: int = None
	unit_id: int = None
	identify_num: int = None
	damage: int = None
	hp: int = None
	energy: int = None
	skill_limit_counter: List[SkillLimitCounter] = None
class TowerSetting(BaseModel):
	initial_energy: int = None
	timeup_hp_penalty: int = None
	timeup_energy_penalty: int = None
	support_rental_cost_coefficient: int = None
	reduce_enemy_energy_value: int = None
	reduce_enemy_energy_lower_limit: int = None
	get_cleared_ex_quest_interval: int = None
	support_lv_band: int = None
	usable_unit_count: int = None
class TowerStatus(BaseModel):
	cleared_floor_num: int = None
	last_login_schedule_id: int = None
class TowerUnit(BaseModel):
	unit_id: int = None
	identify_num: int = None
	hp: int = None
	energy: int = None
	skill_limit_counter: List[SkillLimitCounter] = None
	max_hp: int = None
	saved_hp: int = None
	level: int = None
	rarity: int = None
	promotion_level: int = None
	enemy_color: int = None
	skin_data: SkinData = None
class TowerWaveResultUnitInfo(BaseModel):
	unit_id: int = None
	owner_viewer_id: int = None
	damage: int = None
	is_alive: int = None
class TrainingQuestCount(BaseModel):
	gold_quest: int = None
	exp_quest: int = None
class TtkBeatEnemyInfo(BaseModel):
	enemy_id: int = None
	beat_num: int = None
class TtkCatalogInfo(BaseModel):
	enemy_id: int = None
	total_beat_num: int = None
	status: int = None
class TtkHighScoreInfo(BaseModel):
	normal: int = None
	hard: int = None
	extra: int = None
	endless: int = None
class UekBossInfo(BaseModel):
	enemy_id: int = None
	hp: int = None
	attack_num: int = None
class UniqueEquipLimitSetting(BaseModel):
	equip_slot: int = None
	promotion: int = None
	rarity: int = None
class UniqueEquipSetting(BaseModel):
	limit_list: List[UniqueEquipLimitSetting] = None
class UnitDamageInfo(BaseModel):
	viewer_id: int = None
	unit_id: int = None
	damage: int = None
	rarity: int = None
	skin_data: SkinData = None
class UnitDataForClanMember(BaseModel):
	unit_id: int = None
	position: int = None
	evolution: int = None
	battle_rarity: int = None
	level: int = None
	promotion_level: int = None
	dispatch_count: int = None
	dispatch_status: int = None
	dispatch_start_time: int = None
	current_dispatch_bonus: int = None
	skin_data: SkinData = None
	unique_equipped_list: List[int] = None
class UnitDataForView(BaseModel):
	id: int = None
	unit_level: int = None
	unit_rarity: int = None
	battle_rarity: int = None
	promotion_level: ePromotionLevel = None
	power: int = None
	skin_data: SkinData = None
	unique_equip_slot: List[EquipSlot] = None
class UnitHpInfo(BaseModel):
	viewer_id: int = None
	unit_id: int = None
	hp: int = None
class UnitHpInfoForFriendBattle(BaseModel):
	viewer_id: int = None
	unit_id: int = None
	hp: int = None
	hp_rate: int = None
class UnitOriginalHpInfo(BaseModel):
	viewer_id: int = None
	unit_id: int = None
	hp: int = None
	original_hp: int = None
class UnitParam(BaseModel):
	base_param: StatusParam = None
	equip_param: StatusParam = None
class UnitSetting(BaseModel):
	max_evolution: int = None
	change_to_material: List[IniPair] = None
class UnlockRarity6Slot(BaseModel):
	quest_clear: int = None
	slot_1: int = None
	slot_2: int = None
	slot_3: int = None
	status_1: int = None
	status_2: int = None
	status_3: int = None
class UnreadMessageList(BaseModel):
	equip_requests: List[EquipRequests] = None
class UnreadStoryNoticeSetting(BaseModel):
	time: str = None
	type: int = None
class UsedUnit(BaseModel):
	unit_id: int = None
	full_recovery_time: int = None
	energy: int = None
class UserBirthDayVoice(BaseModel):
	birthday: int = None
	birthday_period: int = None
class UserChara(BaseModel):
	chara_id: int = None
	chara_love: int = None
	love_level: int = None
class UserClan(BaseModel):
	clan_id: int = None
	clan_name: str = None
	latest_request_time: int = None
	donation_num: int = None
	leave_time: int = None
	clan_member_count: int = None
class UserEmblem(BaseModel):
	emblem_id: int = None
	ex_value: int = None
class UserEquipParameter(BaseModel):
	equip_id: int = None
	equip_count: int = None
class UserEquipParameterIdCount(BaseModel):
	id: int = None
	count: int = None
class UserGold(BaseModel):
	gold_id_pay: int = None
	gold_id_free: int = None
class UserInfo(BaseModel):
	viewer_id: int = None
	user_name: str = None
	user_comment: str = None
	emblem: EmblemData = None
	team_level: int = None
	user_stamina: int = None
	team_exp: int = None
	favorite_unit_id: int = None
	tutorial_flag: int = None
	user_birth: int = None
	stamina_full_recovery_time: int = None
	arena_rank: int = None
	invite_accept_flag: int = None
class UserItemParameter(BaseModel):
	item_id: int = None
	item_count: int = None
class UserJewel(BaseModel):
	jewel: int = None
	free_jewel: int = None
class UserMissionInfo(BaseModel):
	mission_id: int = None
	disp_order: int = None
	sort_filter_type: int = None
	mission_status: eMissionStatusType = None
	clear_num: int = None
	team_level: int = None
	receive_status: int = None
	not_exist: bool = None
	is_level_specific_mission: bool = None
class UserMyParty(BaseModel):
	tab_number: int = None
	party_number: int = None
	party_label_type: int = None
	party_name: str = None
	unit_id1: int = None
	unit_id2: int = None
	unit_id3: int = None
	unit_id4: int = None
	unit_id5: int = None
	battle_rarity1: int = None
	battle_rarity2: int = None
	battle_rarity3: int = None
	battle_rarity4: int = None
	battle_rarity5: int = None
class UserMyPartyTab(BaseModel):
	tab_number: int = None
	tab_name: str = None
class UserMyQuest(BaseModel):
	tab_number: int = None
	tab_name: str = None
	skip_count: int = None
	skip_list: List[int] = None
	item_list: List[int] = None
	difficulty_list: List[int] = None
	initial_skip_count: int = None
class UserMyQuestForPost(BaseModel):
	tab_number: int = None
	tab_name: str = None
	skip_count: int = None
	skip_list: List[int] = None
class UserQuestInfo(BaseModel):
	quest_id: int = None
	clear_flg: int = None
	result_type: int = None
	daily_clear_count: int = None
	daily_recovery_count: int = None
class UserSeasonPackInfo(BaseModel):
	mission_id: int = None
	buy_id: int = None
	season_end_time: int = None
	extended: int = None
	received: int = None
	rewards: List[SeasonPackRewardInfo] = None
class UserStaminaInfo(BaseModel):
	user_stamina: int = None
	stamina_full_recovery_time: int = None
class UserStory(BaseModel):
	story_id: int = None
	state: eStoryStatus = None
	pre_watched_flag: int = None
	special_flag: int = None
class VersusResultDetail(BaseModel):
	log_id: int = None
	is_challenge: int = None
	vs_user_team_level: int = None
	vs_user_name: str = None
	win_or_lose: int = None
	emblem: EmblemData = None
	user_arena_deck: List[UnitDataForView] = None
	vs_user_arena_deck: List[UnitDataForView] = None
	damage_list: List[UnitDamageInfo] = None
class VotedUnit(BaseModel):
	rarity1: int = None
	rarity2: int = None
	rarity3: int = None
class VoteRank(BaseModel):
	rank: int = None
	unit_id: int = None
	ratio: int = None
class VoteRanking(BaseModel):
	rarity1: List[VoteRank] = None
	rarity2: List[VoteRank] = None
	rarity3: List[VoteRank] = None
class ArenaWaveResult(BaseModel):
	unit_damage_list: List[UnitDamageInfo] = None
	unit_hp_list: List[UnitHpInfo] = None
	wave_num: int = None
	remain_time: int = None
class BlockUserDetail(BaseModel):
	block_id: int = None
	clan_name: str = None
	team_level: int = None
	owner_name: str = None
	favorite_unit: UnitDataForView = None
	owner_last_login_time: int = None
class BossBattleFinishUnit(BaseModel):
	unit_damage_list: List[UnitDamageInfo] = None
	unit_hp_list: List[UnitHpInfo] = None
class ChatMemberInfo(BaseModel):
	viewer_id: int = None
	name: str = None
	level: int = None
	favorite_unit: UnitDataForView = None
	emblem: EmblemData = None
class ClanBattleFinishUnit(BaseModel):
	unit_damage_list: List[UnitDamageInfo] = None
	unit_hp_list: List[UnitHpInfo] = None
class ClanBattleSuggestDeck(BaseModel):
	total_damage: int = None
	level_id: int = None
	party_type: int = None
	battle_time: int = None
	start_remain_time: int = None
	win_or_lose: int = None
	enc_key: str = None
	deck: List[UnitDataForView] = None
class ClanDetailMemberInfo(BaseModel):
	user_name: str = None
	team_level: int = None
	last_login_time: int = None
	favorite_unit: UnitDataForView = None
class ClanInfo(BaseModel):
	clan_id: int = None
	leader_viewer_id: int = None
	leader_name: str = None
	leader_favorite_unit: UnitDataForView = None
	clan_name: str = None
	description: str = None
	join_condition: eClanJoinCondition = None
	member_num: int = None
	activity: eClanActivityGuideline = None
	grade_rank: int = None
	current_period_ranking: int = None
	clan_battle_mode: int = None
class ClanMemberInfo(BaseModel):
	viewer_id: int = None
	name: str = None
	emblem: EmblemData = None
	role: eClanRole = None
	level: int = None
	favorite_unit: UnitDataForView = None
	dispatch_units: List[UnitDataForClanMember] = None
	last_login_time: int = None
	total_power: int = None
class CounterStopCoinExchange(BaseModel):
	weekly: CounterStopCoinInfo = None
class DailyShop(BaseModel):
	system_id: int = None
	item_list: List[ShopItem] = None
	add_item_list: List[ShopItem] = None
	remaining_appear_count: int = None
	max_appear_num: int = None
class DamageReport(BaseModel):
	viewer_id: int = None
	name: str = None
	favorite_unit: UnitDataForView = None
	damage: int = None
	rank: int = None
	emblem: EmblemData = None
class DeckListDataForView(BaseModel):
	deck_number: int = None
	deck_data_for_view: List[UnitDataForView] = None
class DungeonInfo(BaseModel):
	enter_area_id: int = None
	rest_challenge_count: List[RestChallengeInfo] = None
	dungeon_area: List[DungeonArea] = None
	dungeon_cleared_area_id_list: List[int] = None
class DungeonQueryUnit(BaseModel):
	owner_viewer_id: int = None
	unit_id: int = None
	retired: int = None
	hp: int = None
	energy: int = None
	skill_limit_counter: List[SkillLimitCounter] = None
	parts_list: List[PartsInfo] = None
class DungeonUnit(BaseModel):
	unit_id: int = None
	hp: int = None
	energy: int = None
	skill_limit_counter: int = None
	max_hp: int = None
	power: int = None
	level: int = None
	rarity: int = None
	promotion_level: int = None
	skin_data: SkinData = None
	unique_equipped_list: List[int] = None
	parts_list: List[PartsInfo] = None
class EquipStrSetting(BaseModel):
	lower_rank: int = None
	coin_cost: List[StrCoinCost] = None
	jewel_cost: List[StrJewelCost] = None
class EventEnemyInfo(BaseModel):
	enemy_unit: List[EventSpecialEnemyUnit] = None
	enemy_point: int = None
	seed: int = None
	mode: int = None
	kill_order: List[int] = None
class EventSubStory(BaseModel):
	event_id: int = None
	unlocked: List[int] = None
	read: List[int] = None
	sub_story_info_list: List[EventSubStoryInfo] = None
class FriendBattleResult(BaseModel):
	unit_damage_list: List[UnitDamageInfo] = None
	unit_hp_list: List[UnitHpInfoForFriendBattle] = None
	wave_num: int = None
	remain_time: int = None
class FriendDeckInfo(BaseModel):
	deck_number: int = None
	mask_bif_flag: int = None
	unit_data: List[UnitDataForView] = None
class FriendInfo(BaseModel):
	viewer_id: int = None
	name: str = None
	emblem: EmblemData = None
	level: int = None
	favorite_unit: UnitDataForView = None
	last_login_time: int = None
	total_power: int = None
	friend_num: int = None
class GachaParameter(BaseModel):
	id: int = None
	type: eGachaType = None
	start_time: int = None
	end_time: int = None
	cost_num_single: int = None
	ticket_id: int = None
	free_gacha_interval_time: int = None
	discount_price: int = None
	exchange_id: int = None
	free_exec_times: int = None
	last_free_gacha_time: int = None
	discount_exec_times: int = None
	last_discount_gacha_time: int = None
	recommend_unit: List[RecommendUnit] = None
	url_param: str = None
	ticket_id10: int = None
	selected_item_id: int = None
	bonus_item_list: List[GachaBonusItem] = None
	free_gacha_campaign_id: int = None
	exec_count: int = None
class GrandArenaDamageInfo(BaseModel):
	first_result: List[UnitDamageInfo] = None
	second_result: List[UnitDamageInfo] = None
	third_result: List[UnitDamageInfo] = None
class GrandArenaDeck(BaseModel):
	first: List[UnitDataForView] = None
	second: List[UnitDataForView] = None
	third: List[UnitDataForView] = None
class GrandArenaHistoryDetailInfo(BaseModel):
	log_id: int = None
	is_challenge: int = None
	vs_user_viewer_id: int = None
	vs_user_team_level: int = None
	vs_user_name: str = None
	win_or_lose: List[int] = None
	emblem: EmblemData = None
	user_grand_arena_deck: GrandArenaDeck = None
	vs_user_grand_arena_deck: GrandArenaDeck = None
	damage_list: GrandArenaDamageInfo = None
class GrandArenaOppnentUserInfo(BaseModel):
	viewer_id: int = None
	user_name: str = None
	team_level: int = None
	favorite_unit: UnitDataForView = None
	total_power: int = None
	emblem: EmblemData = None
class GrandArenaSearchOpponent(BaseModel):
	null: int = None
	viewer_id: int = None
	rank: int = None
	winning_number: int = None
	user_name: str = None
	team_level: int = None
	favorite_unit: UnitDataForView = None
	emblem: EmblemData = None
	grand_arena_deck: GrandArenaDeck = None
class GrowthInfo(BaseModel):
	unit_id: int = None
	growth_parameter_list: GrowthParameterList = None
class HatsuneBossBattleFinishUnit(BaseModel):
	unit_damage_list: List[UnitDamageInfo] = None
	unit_hp_list: List[UnitOriginalHpInfo] = None
class HistoryReport(BaseModel):
	viewer_id: int = None
	unit_id: int = None
	unit_rarity: int = None
	damage: int = None
	skin_data: SkinData = None
class InviteClanDetail(BaseModel):
	clan_id: int = None
	leader_viewer_id: int = None
	invite_id: int = None
	leader_name: str = None
	leader_favorite_unit: UnitDataForView = None
	clan_name: str = None
	description: str = None
	invite_message: str = None
	join_condition: eClanJoinCondition = None
	activity: eClanActivityGuideline = None
	clan_battle_mode: int = None
	member_num: int = None
	grade_rank: int = None
class InvitedUserDetail(BaseModel):
	viewer_id: int = None
	invite_id: int = None
	user_name: str = None
	favorite_unit: UnitDataForView = None
	team_level: int = None
	user_last_login_time: int = None
	emblem: EmblemData = None
class JoinRequestUserInfo(BaseModel):
	viewer_id: int = None
	name: str = None
	level: int = None
	comment: str = None
	favorite_unit: UnitDataForView = None
	emblem: EmblemData = None
class MemberBossRanks(BaseModel):
	name: str = None
	favorite_unit: UnitDataForView = None
	emblem: EmblemData = None
	bosses: List[BossRank] = None
	viewer_id: int = None
	score: int = None
class MemberScoreRanking(BaseModel):
	name: str = None
	favorite_unit: UnitDataForView = None
	rank: int = None
	score: int = None
	total_power: int = None
	emblem: EmblemData = None
	viewer_id: int = None
class MyLogUnitData(BaseModel):
	unit_id: int = None
	unit_rarity: int = None
	unit_level: int = None
	promotion_level: int = None
	damage: int = None
	skin_data: SkinData = None
	unique_equip_slot: List[EquipSlot] = None
	viewer_id: int = None
class MyPartyInfo(BaseModel):
	tab: UserMyPartyTab = None
	party: List[UserMyParty] = None
class NormalGachaSetting(BaseModel):
	term_list: List[NormalGachaTerm] = None
class OpponentUser(BaseModel):
	viewer_id: int = None
	user_name: str = None
	team_level: int = None
	favorite_unit: UnitDataForView = None
	total_power: int = None
	emblem: EmblemData = None
class OtherClanData(BaseModel):
	detail: ClanInfo = None
	members: List[ClanMemberInfo] = None
	invite_id: int = None
	block_id: int = None
class PeriodRanking(BaseModel):
	clan_name: str = None
	member_num: int = None
	leader_viewer_id: int = None
	leader_name: str = None
	emblem: EmblemData = None
	leader_favorite_unit: UnitDataForView = None
	rank: int = None
	damage: int = None
	grade_rank: int = None
class PkbBattingResultInfo(BaseModel):
	batting_distance: int = None
	replay: PkbReplay = None
class PkbCatalogInfo(BaseModel):
	batter: List[PkbCatalogBatter] = None
	pitcher: List[PkbCatalogPitcher] = None
class PkbRankingRecordSingle(BaseModel):
	record_value: int = None
	status: int = None
	replay: PkbReplay = None
class PkbRankingRecordTotal(BaseModel):
	record_value: int = None
	status: int = None
	replay_list: List[PkbReplay] = None
class PkbRankingSingle(BaseModel):
	normal: List[PkbRankingRecordSingle] = None
	hard: List[PkbRankingRecordSingle] = None
	very_hard: List[PkbRankingRecordSingle] = None
	extra: List[PkbRankingRecordSingle] = None
class PkbRankingTotal(BaseModel):
	normal: List[PkbRankingRecordTotal] = None
	hard: List[PkbRankingRecordTotal] = None
	very_hard: List[PkbRankingRecordTotal] = None
	extra: List[PkbRankingRecordTotal] = None
class QuestReplayData(BaseModel):
	clear_flg: int = None
	team_level: int = None
	power: int = None
	seed: int = None
	enc_key: str = None
	unit_info: List[UnitDataForView] = None
class RankingSearchOpponent(BaseModel):
	viewer_id: int = None
	rank: int = None
	user_name: str = None
	team_level: int = None
	favorite_unit: UnitDataForView = None
	arena_deck: List[UnitDataForView] = None
	emblem: EmblemData = None
class ReplayUnitDataForView(BaseModel):
	id: int = None
	unit_level: int = None
	unit_rarity: int = None
	battle_rarity: int = None
	promotion_level: ePromotionLevel = None
	skin_data: SkinData = None
	unique_equip_slot: List[EquipSlot] = None
	is_alive: int = None
class RequiredMaterialList(BaseModel):
	equip_list: List[UserEquipParameterIdCount] = None
class RoomFloorLayout(BaseModel):
	floor: List[RoomItemPosition] = None
	wall: List[RoomItemPosition] = None
	theme: RoomTheme = None
class RoomFloorLayoutForMyset(BaseModel):
	floor: List[RoomItemPositionForMyset] = None
	wall: List[RoomItemPositionForMyset] = None
	theme: RoomTheme = None
class RoomUserInfo(BaseModel):
	viewer_id: int = None
	name: str = None
	comment: str = None
	team_level: int = None
	today_like_flag: bool = None
	like_time: int = None
	flag_read: bool = None
	total_liked: int = None
	like_reward: int = None
	favorite_unit: UnitDataForView = None
	deck_list_for_client: List[DeckListDataForView] = None
	emblem: EmblemData = None
class RoomWholeLayout(BaseModel):
	background_theme: int = None
	floor_layout: List[RoomFloorLayout] = None
class RoomWholeLayoutForMyset(BaseModel):
	background_theme: int = None
	floor_layout: RoomFloorLayoutForMyset = None
class SekaiRanking(BaseModel):
	name: str = None
	favorite_unit: UnitDataForView = None
	rank: int = None
	damage: int = None
	total_power: int = None
class ShioriQuestInfo(BaseModel):
	quest_list: List[UserQuestInfo] = None
	dead_boss_list: List[int] = None
class ShopInfo(BaseModel):
	system_id: int = None
	reset_count: int = None
	next_renewal_time: int = None
	reset_cost: int = None
	reset_cost_id: int = None
	close_time: int = None
	remaining_appear_count: int = None
	max_appear_num: int = None
	item_list: List[ShopItem] = None
class SpecialBattleInfo(BaseModel):
	enemy_unit: List[UnitHpInfo] = None
	enemy_point: int = None
	mode: int = None
	kill_limit: int = None
class TowerClearedUserInfo(BaseModel):
	viewer_id: int = None
	user_name: str = None
	team_level: int = None
	favorite_unit: UnitDataForView = None
	cleared_time: int = None
	emblem: EmblemData = None
class TowerReplayPartyInfo(BaseModel):
	power: int = None
	unit_info: List[ReplayUnitDataForView] = None
class TowerReplayPartyStatusList(BaseModel):
	party_status1: List[TowerUnit] = None
	party_status2: List[TowerUnit] = None
	party_status3: List[TowerUnit] = None
class TowerReplaySummary(BaseModel):
	team_level: int = None
	win_party: int = None
	enc_key: str = None
	party_list: List[TowerReplayPartyInfo] = None
class TowerWaveResultInfo(BaseModel):
	wave_num: int = None
	unit_info_list: List[TowerWaveResultUnitInfo] = None
	remain_time: int = None
class TutorialGachaIndex(BaseModel):
	gacha_info: List[GachaParameter] = None
class TutorialHomeIndex(BaseModel):
	mission_count: int = None
	unread_message_count: int = None
	user_clan: UserClan = None
class TutorialMissionIndex(BaseModel):
	missions: List[UserMissionInfo] = None
	daily_reset_time: int = None
class UnitData(BaseModel):
	id: int = None
	get_time: int = None
	start_rarety: int = None
	unit_rarity: int = None
	battle_rarity: int = None
	unit_level: int = None
	unit_exp: int = None
	exceed_stage: int = None
	promotion_level: ePromotionLevel = None
	union_burst: List[SkillLevelInfo] = None
	main_skill: List[SkillLevelInfo] = None
	ex_skill: List[SkillLevelInfo] = None
	free_skill: List[SkillLevelInfo] = None
	equip_slot: List[EquipSlot] = None
	unique_equip_slot: List[EquipSlot] = None
	unit_param: UnitParam = None
	bonus_param: StatusParamShort = None
	resist_status_id: int = None
	power: int = None
	skin_data: SkinData = None
	identify_num: int = None
	favorite_flag: int = None
	unlock_rarity_6_item: UnlockRarity6Slot = None
	total_hp: int = None
	total_atk: int = None
	total_def: int = None
	total_magic_atk: int = None
	total_magic_def: int = None
	total_critical: int = None
	total_magic_critical: int = None
	total_wave_hp_recovery: int = None
	total_wave_energy_recovery: int = None
	total_hp_recovery_rate: int = None
	total_physical_penetrate: int = None
	total_magic_penetrate: int = None
	total_life_steal: int = None
	total_dodge: int = None
	total_accuracy: int = None
	total_energy_recovery_rate: int = None
	total_energy_reduce_rate: int = None
class UnitDataLight(BaseModel):
	id: int = None
	get_time: int = None
	start_rarety: int = None
	unit_rarity: int = None
	battle_rarity: int = None
	unit_level: int = None
	unit_exp: int = None
	promotion_level: ePromotionLevel = None
	union_burst: List[SkillLevelInfoLight] = None
	main_skill: List[SkillLevelInfoLight] = None
	ex_skill: List[SkillLevelInfoLight] = None
	equip_slot: List[EquipSlotLight] = None
	unique_equip_slot: List[EquipSlotLight] = None
	bonus_param: StatusParamShort = None
	resist_status_id: int = None
	power: int = None
	skin_data: SkinData = None
	identify_num: int = None
	favorite_flag: int = None
	unlock_rarity6_item: UnlockRarity6Slot = None
class VersusResult(BaseModel):
	log_id: int = None
	versus_time: int = None
	win_or_lose: int = None
	opponent_user: OpponentUser = None
class ArenaWaveInfo(BaseModel):
	user_arena_deck: List[UnitData] = None
	vs_user_arena_deck: List[UnitData] = None
	seed: int = None
	battle_log_id: int = None
	wave_num: int = None
class BossRankingInClanPhase(BaseModel):
	phase_num: int = None
	enemy_id: int = None
	my_rank_pos: int = None
	ranking: List[MemberScoreRanking] = None
class BossRankingInClanSummaryPhase(BaseModel):
	phase_num: int = None
	my_member_pos: int = None
	members: List[MemberBossRanks] = None
class ClanBattleSupportUnit(BaseModel):
	unit_data: UnitData = None
	current_support_unit: int = None
	owner_viewer_id: int = None
	owner_name: str = None
	remaining_count: int = None
class ClanBattleSupportUnitLight(BaseModel):
	unit_data: UnitDataLight = None
	current_support_unit: int = None
	owner_viewer_id: int = None
	owner_name: str = None
	remaining_count: int = None
class ClanData(BaseModel):
	detail: ClanInfo = None
	members: List[ClanMemberInfo] = None
class ClanDispatchUnit(BaseModel):
	owner_viewer_id: int = None
	owner_name: str = None
	enable: int = None
	current_support_unit: int = None
	hp: int = None
	energy: int = None
	unit_data: UnitData = None
class ClanDispatchUnitLight(BaseModel):
	current_support_unit: int = None
	enable: int = None
	energy: int = None
	hp: int = None
	owner_name: str = None
	owner_viewer_id: int = None
	unit_data: UnitDataLight = None
class DungeonQuest(BaseModel):
	quest_id: int = None
	open_chest: int = None
	limit_time: int = None
	background: int = None
	chest_id: int = None
	versus_viewer_id: int = None
	team_level: int = None
	clan_name: str = None
	name: str = None
	versus_unit_list: List[DungeonUnit] = None
class EventSpecialBattleExHistory(BaseModel):
	attack_num: int = None
	total_power: int = None
	damage: int = None
	mode: int = None
	unit_data: List[ReplayUnitDataForView] = None
	manual_flags: int = None
class FriendBattleInfo(BaseModel):
	viewer_id: int = None
	name: str = None
	emblem: EmblemData = None
	level: int = None
	favorite_unit: UnitDataForView = None
	deck_list: List[FriendDeckInfo] = None
class GachaGrowthUnitInfo(BaseModel):
	growth1: GrowthInfo = None
	growth2: GrowthInfo = None
	growth3: GrowthInfo = None
	growth4: GrowthInfo = None
	growth5: GrowthInfo = None
	growth6: GrowthInfo = None
	growth7: GrowthInfo = None
	growth8: GrowthInfo = None
	growth9: GrowthInfo = None
	growth10: GrowthInfo = None
class GachaStep(BaseModel):
	gacha_index: TutorialGachaIndex = None
class GrandArenaHistoryInfo(BaseModel):
	log_id: int = None
	versus_time: int = None
	is_challenge: int = None
	win_or_lose: int = None
	emblem: EmblemData = None
	win_number: int = None
	lose_number: int = None
	opponent_user: GrandArenaOppnentUserInfo = None
class IniSetting(BaseModel):
	equipment_enhance: EquipStrSetting = None
	quest: QuestSetting = None
	dungeon: DungeonSetting = None
	unit: UnitSetting = None
	arena: ArenaSetting = None
	grand_arena: GrandArenaSetting = None
	limit: LimitSetting = None
	clan: ClanSetting = None
	clan_battle: ClanBattleSetting = None
	friend: FriendSetting = None
	room: RoomSetting = None
	tower: TowerSetting = None
	recover_challenge_count: RecoverChallengeCountSetting = None
	very_hard_recover_challenge_count: RecoverChallengeCountSetting = None
	send_api: SendApi = None
	battle_log_type: BattleLogType = None
	normal_gacha: NormalGachaSetting = None
	require_exchange_point: int = None
	hatsune_recover_challenge_count: RecoverChallengeCountSetting = None
	cartoon: CartoonSetting = None
	unique_equip: UniqueEquipSetting = None
	equip_recover_challenge_count: RecoverChallengeCountSetting = None
	high_rarity_equip_recover_challenge_count: RecoverChallengeCountSetting = None
	unread_story_notice: UnreadStoryNoticeSetting = None
	max_boss_battle_skip_num: int = None
	max_gacha_count: int = None
	multiple_skip: BulkSkipSetting = None
	friend_support_unit: FriendSupportUnitIniSetting = None
	kaiser_battle: KaiserBattleIniSetting = None
	serial_code: SerialCodeIniSetting = None
	arena_skip_upper_rank: int = None
	loop_box_multi_gacha_count: int = None
class InventoryInfo(BaseModel):
	id: int = None
	type: eInventoryType = None
	count: int = None
	received: int = None
	stock: int = None
	unit_data: UnitData = None
	exchange_data: DuplicateUnitInfo = None
class MyLog(BaseModel):
	mylog_id: int = None
	battle_log_id: int = None
	is_auto: int = None
	lap_num: int = None
	phase_num: int = None
	order_num: int = None
	battle_time: int = None
	total_damage: int = None
	units: List[MyLogUnitData] = None
	enemy: MyLogEnemyData = None
	clan_battle_mode: int = None
class PkbRankingInfo(BaseModel):
	single_distance: PkbRankingSingle = None
	total_distance: PkbRankingTotal = None
	home_run_num: PkbRankingTotal = None
class PracticeWaveInfo(BaseModel):
	battle_log_id: int = None
	seed: int = None
	user_deck: List[UnitData] = None
	vs_user_deck: List[UnitData] = None
	wave_num: int = None
class PrizeRewardInfoDetail(BaseModel):
	rarity: int = None
	rewards: List[InventoryInfo] = None
class QuestResult(BaseModel):
	reward_list: List[InventoryInfo] = None
	acquired_gold: int = None
	acquired_team_exp: int = None
	acquired_gold_list: List[SkipGoldRewardInfo] = None
class QuestResultList(BaseModel):
	quest_result: List[QuestResult] = None
	quest_id: int = None
	daily_clear_count: int = None
class RankingReward(BaseModel):
	rank_from: int = None
	rank_to: int = None
	reward_list: List[InventoryInfo] = None
class RoomMysetElement(BaseModel):
	myset_index: int = None
	myset_name: str = None
	myset_update_time: str = None
	myset_layout: RoomWholeLayoutForMyset = None
class SearchOpponent(BaseModel):
	viewer_id: int = None
	rank: int = None
	user_name: str = None
	team_level: int = None
	favorite_unit: UnitDataForView = None
	arena_deck: List[UnitData] = None
	emblem: EmblemData = None
class SupportUnitForProfile(BaseModel):
	position: int = None
	unit_data: UnitDataLight = None
class SupportUnitStatus(BaseModel):
	owner_name: str = None
	owner_viewer_id: int = None
	unit_data: UnitDataLight = None
	user_position_status: int = None
	unit_param_data: UnitData = None
class TowerClanMemberInfo(BaseModel):
	cleared_data: TowerClearedUserInfo = None
	floor_num: int = None
	cleared_ex_quest_list: List[ClearedExQuestList] = None
	cloister_cleared_time: int = None
class TowerExDispatchUnit(BaseModel):
	owner_viewer_id: int = None
	owner_name: str = None
	enable: int = None
	current_support_unit: int = None
	unit_data: UnitData = None
class TowerExDispatchUnitLight(BaseModel):
	owner_viewer_id: int = None
	owner_name: str = None
	enable: int = None
	current_support_unit: int = None
	unit_data: UnitDataLight = None
class TowerExPartyInfo(BaseModel):
	first: List[UnitData] = None
	second: List[UnitData] = None
	third: List[UnitData] = None
class TowerReplayPartyList(BaseModel):
	party1: List[UnitData] = None
	party2: List[UnitData] = None
	party3: List[UnitData] = None
class TutorialGachaExec(BaseModel):
	reward_info_list: List[InventoryInfo] = None
	add_present_count: int = None
class TutorialMissionAccept(BaseModel):
	team_level: int = None
	team_exp: int = None
	stamina_info: UserStaminaInfo = None
	rewards: List[InventoryInfo] = None
	flag_exchange_team_exp: bool = None
	add_present_count: int = None
class TutorialQuestFinish(BaseModel):
	level_info: LevelInfo = None
	user_info: UserStaminaInfo = None
	flag_exchange_team_exp: bool = None
	unlock_quest_list: List[int] = None
	open_story_ids: List[UserStory] = None
	quest_id: int = None
	clear_flag: int = None
	result_type: int = None
	daily_clear_count: int = None
	rewards: List[InventoryInfo] = None
	add_present_count: int = None
class TutorialUnitEquip(BaseModel):
	unit_data: UnitData = None
	equip_data: InventoryInfo = None
class WaveEnemyInfo(BaseModel):
	enemy_id: int = None
	drop_gold: int = None
	drop_reward: List[InventoryInfo] = None
class WaveEnemyInfoList(BaseModel):
	enemy_info_list: List[WaveEnemyInfo] = None
class AlchemyReward(BaseModel):
	reward_info_list: List[InventoryInfo] = None
class BossRankingInClan(BaseModel):
	order_num: int = None
	latest_phase_num: int = None
	phases: List[BossRankingInClanPhase] = None
class BossRankingInClanSummary(BaseModel):
	latest_phase_num: int = None
	phases: List[BossRankingInClanSummaryPhase] = None
class BossReward(BaseModel):
	clan_battle_id: int = None
	lap_num: int = None
	id: int = None
	kill_time: int = None
	reward_info: List[InventoryInfo] = None
class ClanBattleExtraBattleChallengeRewardInfo(BaseModel):
	challenge_count: int = None
	reward_info: List[InventoryInfo] = None
class ClearRewardInfo(BaseModel):
	type: int = None
	reward_info: List[InventoryInfo] = None
class EquipDonateNotification(BaseModel):
	donation_list: List[EquipDonate] = None
	equip_list: List[InventoryInfo] = None
	request: EquipRequests = None
class EquipStep(BaseModel):
	unit_equip1: TutorialUnitEquip = None
	unit_equip2: TutorialUnitEquip = None
class GachaBonusResult(BaseModel):
	bonus_1: InventoryInfo = None
	bonus_2: InventoryInfo = None
	bonus_3: InventoryInfo = None
	bonus_4: InventoryInfo = None
	bonus_5: InventoryInfo = None
	bonus_6: InventoryInfo = None
	bonus_7: InventoryInfo = None
	bonus_8: InventoryInfo = None
	bonus_9: InventoryInfo = None
	bonus_10: InventoryInfo = None
class GachaPrizeItemDetail(BaseModel):
	rarity: int = None
	odds: float = None
	odds_in10th: float = None
	reward_list: List[InventoryInfo] = None
class HatsuneLoginBonusData(BaseModel):
	todays_count: int = None
	rewards: List[InventoryInfo] = None
class MissionStep(BaseModel):
	mission_index: TutorialMissionIndex = None
	mission_accept: TutorialMissionAccept = None
class Notification(BaseModel):
	equip_donation: EquipDonateNotification = None
	mission: List[MissionNotice] = None
class PrizeRewardInfo(BaseModel):
	prize_1: PrizeRewardInfoDetail = None
	prize_2: PrizeRewardInfoDetail = None
	prize_3: PrizeRewardInfoDetail = None
	prize_4: PrizeRewardInfoDetail = None
	prize_5: PrizeRewardInfoDetail = None
	prize_6: PrizeRewardInfoDetail = None
	prize_7: PrizeRewardInfoDetail = None
	prize_8: PrizeRewardInfoDetail = None
	prize_9: PrizeRewardInfoDetail = None
	prize_10: PrizeRewardInfoDetail = None
class TutorialQuestStart(BaseModel):
	quest_wave_info: List[WaveEnemyInfoList] = None
	limit_time: int = None
	quest_id: int = None
	enemy_list: List[UnitData] = None
	user_info: UserStaminaInfo = None
	battle_log_id: int = None
class TutorialStoryQuestStart(BaseModel):
	quest_wave_info: List[WaveEnemyInfoList] = None
	limit_time: int = None
	quest_id: int = None
	enemy_list: List[UnitData] = None
	user_info: UserStaminaInfo = None
	guest_data: List[UnitData] = None
class PrologueFirstStep(BaseModel):
	story_quest_start: TutorialStoryQuestStart = None
class PrologueLatterDStep(BaseModel):
	story_quest_start: TutorialStoryQuestStart = None
class QuestOneStep(BaseModel):
	home_index: TutorialHomeIndex = None
	quest_start: TutorialQuestStart = None
	quest_finish: TutorialQuestFinish = None
class QuestTwoStep(BaseModel):
	gacha_exec: TutorialGachaExec = None
	home_index: TutorialHomeIndex = None
	quest_start: TutorialQuestStart = None
	quest_finish: TutorialQuestFinish = None
