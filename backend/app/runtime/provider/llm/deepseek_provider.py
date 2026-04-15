from loguru import logger
from typing import Optional


class DeepSeekProvider:
    provider_name: str = "deepseek"

    async def chat(self, messages: list, **kwargs) -> str:
        logger.debug("DeepSeek chat stub")
        return ""
