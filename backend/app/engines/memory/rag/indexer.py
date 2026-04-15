from loguru import logger
from typing import List


class Indexer:
    async def index(self, text: str, metadata: dict = None) -> List[str]:
        logger.debug("Indexer index stub")
        return []
