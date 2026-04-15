from typing import Optional


class AvatarManager:
    async def get_avatar(self, user_id: str) -> Optional[dict]:
        return None

    async def update_avatar(self, user_id: str, config: dict) -> dict:
        return {"status": "updated"}
