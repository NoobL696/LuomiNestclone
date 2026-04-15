from loguru import logger
from typing import Optional


class KnowledgeGraph:
    async def add_entity(self, entity: dict) -> None:
        logger.debug(f"KnowledgeGraph add_entity stub")

    async def query(self, entity_id: str) -> Optional[dict]:
        return None
