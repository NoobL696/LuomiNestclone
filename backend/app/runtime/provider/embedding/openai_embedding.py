from loguru import logger
from typing import List


class OpenAIEmbeddingProvider:
    provider_name: str = "openai_embedding"

    async def embed(self, text: str) -> list[float]:
        logger.debug("OpenAI embedding stub")
        return []
