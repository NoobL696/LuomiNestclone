from loguru import logger


class Persona:
    async def get_persona(self, user_id: str) -> dict:
        return {"name": "Luomi", "style": "friendly"}

    async def update_persona(self, user_id: str, config: dict) -> dict:
        return {"status": "updated"}
