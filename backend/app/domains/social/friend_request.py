from loguru import logger


class FriendRequest:
    async def send(self, from_user: str, to_user: str) -> dict:
        return {"status": "sent"}

    async def accept(self, request_id: str) -> dict:
        return {"status": "accepted"}
