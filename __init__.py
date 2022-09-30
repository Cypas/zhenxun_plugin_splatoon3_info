import json
from .splatoon3 import RegularSchedules, BankaraChallengeSchedules,BankaraOpenSchedules, CoopGroupingSchedule
from nonebot.adapters.onebot.v11 import GROUP, Bot, GroupMessageEvent, Message
from nonebot.params import CommandArg
from nonebot import on_command
from nonebot.matcher import Matcher
from utils.message_builder import custom_forward_msg

__zx_plugin_name__ = "splatoon3日程"
__plugin_usage__ = """
指令：
    /工
    /涂地
    /真格
    其实/换成.也可以
""".strip()
__plugin_des__ = "提供splatoon3日程查询"
__plugin_cmd__ = ["\/工/\/打工.工.打工"
                  "\/涂地\/地.涂地.地"
                  "\/真格.真格"]
__plugin_type__ = ("一些工具", 1)
__plugin_version__ = 1.0
__plugin_author__ = "Cypas"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["/工",
            "/涂地",
            "/真格"],
}

gong = on_command(
    "/工", aliases={"/打工", ".工", ".打工"}, permission=GROUP, priority=5, block=True
)
tudi = on_command(
    "/涂地", aliases={"/地", ".涂地", ".地"}, permission=GROUP, priority=5, block=True
)
zhenge = on_command(
    "/真格", aliases={".真格"}, permission=GROUP, priority=5, block=True
)


@gong.handle()
async def _(
        bot: Bot, event: GroupMessageEvent, matcher: Matcher, arg: Message = CommandArg()
):
    data = json.loads(splatoon3.get_json('https://splatoon3.ink/data/schedules.json'))
    msg=splatoon3.CoopGroupingSchedule(data, 0)
    msg = Message(msg)
    matcher.finish(msg)



@tudi.handle()
async def _(
        bot: Bot, event: GroupMessageEvent, matcher: Matcher, arg: Message = CommandArg()
):
    data = json.loads(splatoon3.get_json('https://splatoon3.ink/data/schedules.json'))
    msg_list = []
    msg_list.append(splatoon3.RegularSchedules(data, 0))
    msg_list.append(splatoon3.RegularSchedules(data, 1))
    msg_list.append(splatoon3.RegularSchedules(data, 2))
    msg_list.append(splatoon3.RegularSchedules(data, 3))
    msg = custom_forward_msg(msg_list, bot.self_id)
    await bot.send_group_forward_msg(group_id=event.group_id, messages=msg)


@zhenge.handle()
async def _(
        bot: Bot, event: GroupMessageEvent, matcher: Matcher, arg: Message = CommandArg()
):
    data = json.loads(splatoon3.get_json('https://splatoon3.ink/data/schedules.json'))
    msg_list = []
    msg_list.append(splatoon3.BankaraChallengeSchedules(data, 0))
    msg_list.append(splatoon3.BankaraOpenSchedules(data, 0))
    msg_list.append(splatoon3.BankaraChallengeSchedules(data, 1))
    msg_list.append(splatoon3.BankaraOpenSchedules(data, 1))
    msg = custom_forward_msg(msg_list, bot.self_id)
    await bot.send_group_forward_msg(group_id=event.group_id, messages=msg)
