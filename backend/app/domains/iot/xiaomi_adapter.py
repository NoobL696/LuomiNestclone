from loguru import logger


class XiaomiAdapter:
    async def get_device_status(self, did: str) -> dict:
        return {"did": did, "status": "unknown"}

    async def control_device(self, did: str, action: str, params: dict = None) -> dict:
        logger.debug(f"Xiaomi control: {did} -> {action}")
        return {"status": "ok"}
