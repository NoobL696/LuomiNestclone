from loguru import logger
from typing import List, Optional


class ContactManager:
    async def list_contacts(self) -> List[dict]:
        return []

    async def add_contact(self, name: str, platform: str) -> dict:
        return {"status": "added"}
