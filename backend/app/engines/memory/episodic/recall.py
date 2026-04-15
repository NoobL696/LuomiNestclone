from loguru import logger
from typing import List, Optional


class Recall:
    async def recall(self, query: str, user_id: str, top_k: int = 5) -> List[dict]:
        logger.debug(f"Recall: {query}")
        return []
