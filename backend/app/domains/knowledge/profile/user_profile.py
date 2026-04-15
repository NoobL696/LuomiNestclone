from loguru import logger
from typing import Optional


class UserProfile:
    async def get(self, user_id: str) -> Optional[dict]:
        return None

    async def update(self, user_id: str, data: dict) -> dict:
        return {"status": "updated"}
