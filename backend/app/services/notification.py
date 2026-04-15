from typing import Optional


class NotificationService:
    async def send(self, user_id: str, title: str, body: str) -> dict:
        return {"status": "sent"}

    async def list_notifications(self, user_id: str) -> list:
        return []
