import random
from astrbot.api.star import Context, Star, register
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.event.filter import event_message_type, EventMessageType


text_list = [
    "番茄鼻屎",
    "番茄猪肉",
    "番茄鸡肉",
    "番茄炒蛋",
    "番茄鸡蛋",
    "番茄牛肉",
    "番茄米粉",
    "番茄米饭",
    "番茄炒逼",
    "番茄炒屎",
    "番茄炒尿",
    "番茄炒水",
    "番茄三明治",
    "番茄苞豆",
    "番茄炒河粉",
    "番茄炒米粉",
    "番茄豆腐",
    "番茄香肠",
    "番茄暴扣",
    "番茄大灌篮！",
    "番茄包皮垢",
    "番茄炒屁股",
    "番茄炒胸",
    "番茄炒男同",
    "番茄炒女同",
    "番茄炒处女",
    "番茄炒处男",
    "番茄炒丛雨",
    "番茄炒宁宁",
    "番茄炒你妈",
    "番茄炒你爸",
    "番茄炒包皮",
    "番茄炒阴蒂",
    "番茄炒阴道",
    "番茄炒尿道",
    "番茄炒屁眼",
    "番茄炒头发",
    "番茄炒耳屎",
    "番茄炒月经",
    "吃你妈，吃屎去吧！"
]

@register("AstrBot_chishenme", "mingrixiangnai", "今天吃什么", "1.0", "https://github.com/mingrixiangnai/chishenme")
class GenshinImpactPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @event_message_type(EventMessageType.ALL)
    async def on_message(self, event: AstrMessageEvent) -> MessageEventResult:
        """
        当消息中包含“吃什么”时随机发送上面的一条消息。
        """
        msg_obj = event.message_obj
        text = msg_obj.message_str or ""

        if "吃什么" in text:
            # 随机抽取text_list中的一条
            selected_text = random.choice(text_list)
            yield event.plain_result(selected_text)
