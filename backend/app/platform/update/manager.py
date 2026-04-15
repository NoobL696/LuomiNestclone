from loguru import logger


class UpdateManager:
    async def check_update(self) -> dict:
        return {"has_update": False, "version": "0.0.0"}

    async def apply_update(self, version: str) -> dict:
        logger.debug(f"UpdateManager apply: {version}")
        return {"status": "updated"}
