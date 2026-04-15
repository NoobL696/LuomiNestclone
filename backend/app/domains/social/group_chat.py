from loguru import logger
from typing import List


class GroupChat:
    async def create(self, name: str, members: List[str]) -> dict:
        return {"id": "stub", "name": name}

    async def send_message(self, group_id: str, message: str) -> dict:
        return {"status": "sent"}
