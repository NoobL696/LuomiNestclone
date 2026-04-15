from loguru import logger
from typing import List


class Retriever:
    async def retrieve(self, query: str, top_k: int = 5) -> List[dict]:
        logger.debug(f"Retriever retrieve: {query}")
        return []
