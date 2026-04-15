from loguru import logger


class CustomDevice:
    async def register(self, device_config: dict) -> dict:
        return {"status": "registered"}

    async def control(self, device_id: str, command: str) -> dict:
        logger.debug(f"CustomDevice control: {device_id} -> {command}")
        return {"status": "ok"}
