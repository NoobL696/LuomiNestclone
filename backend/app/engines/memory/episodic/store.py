from loguru import logger
from typing import Optional


class EpisodicStore:
    async def store(self, memory: dict) -> str:
        return "stub_id"

    async def get(self, memory_id: str) -> Optional[dict]:
        return None
