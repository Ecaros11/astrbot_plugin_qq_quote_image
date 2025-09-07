from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.core.message.components import Record


@register(
    "astrbot_plugin_quote_enhance",     # 插件ID
    "Gemini & Ecaros11",                # 作者
    "自动将引用消息的上下文加入LLM请求中",  # 插件描述
    "1.0.0",                            # 版本號
)
class SyaSthPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        logger.info("说话插件已加载，监听 LLM 请求。")

    # 这个形式定义的工具函数会被自动加载到 AstrBot Core 中，在 Core 请求大模型时会被自动带上。
    @filter.llm_tool(name="say_sth") # 如果 name 不填，将使用函数名
    async def say_sth(self, event: AstrMessageEvent, say_str: str) -> MessageEventResult:
        '''说话工具。当你需要说些什么时，请使用此工具。

        Args:
            say_str(string): 要说的话（例如：你好呀，我是雨末末）
        '''

        if tts := self.context.get_using_tts_provider():
            if audio_path := await tts.get_audio(say_str):
                yield event.chain_result([Record(audio_path)])