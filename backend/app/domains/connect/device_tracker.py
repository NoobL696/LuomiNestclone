from loguru import logger


class DeviceTracker:
    async def get_location(self, device_id: str) -> dict:
        return {"device_id": device_id, "location": "unknown"}

    async def track(self, device_id: str, location: dict) -> None:
        logger.debug(f"DeviceTracker track: {device_id}")
