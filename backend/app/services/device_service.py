from typing import Optional, List


class DeviceService:
    async def list_devices(self) -> List[dict]:
        return []

    async def get_device(self, device_id: str) -> Optional[dict]:
        return None

    async def register_device(self, device_data: dict) -> dict:
        return {"status": "registered"}
