from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.provider import ProviderRequest


@register(
    "astrbot_plugin_quote_enhance",     # 插件ID
    "Gemini & Ecaros11",                # 作者
    "自动将引用消息的上下文加入LLM请求中",  # 插件描述
    "1.0.0",                            # 版本號
)
class QuoteEnhancePlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        logger.info("引用增强插件已加载，监听 LLM 请求。")
    
    # 在调用 LLM 前，会触发
    @filter.on_llm_request() 
    async def my_custom_hook_1(self, event: AstrMessageEvent, req: ProviderRequest):
        """
        监听 on_llm_request 钩子，在 LLM 被调用前修改请求。
        """

        logger.info(event.message_obj)
