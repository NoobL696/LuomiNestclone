from loguru import logger
from typing import Optional, List


class DeviceHub:
    async def list_devices(self) -> List[dict]:
        return []

    async def get_device(self, device_id: str) -> Optional[dict]:
        return None

    async def control(self, device_id: str, action: str, params: dict = None) -> dict:
        logger.debug(f"DeviceHub control: {device_id} -> {action}")
        return {"status": "ok"}
