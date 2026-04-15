from loguru import logger
from typing import Optional


class OpenAIProvider:
    provider_name: str = "openai"

    async def chat(self, messages: list, **kwargs) -> str:
        logger.debug("OpenAI chat stub")
        return ""

    async def stream_chat(self, messages: list, **kwargs):
        yield ""
