from loguru import logger
from typing import Optional


class SessionStore:
    async def save(self, session_id: str, data: dict) -> None:
        logger.debug(f"SessionStore save: {session_id}")

    async def load(self, session_id: str) -> Optional[dict]:
        return None
