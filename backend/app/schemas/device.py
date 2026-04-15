from pydantic import BaseModel
from typing import Optional


class DeviceBase(BaseModel):
    name: str
    device_type: str
    protocol: Optional[str] = None


class DeviceResponse(DeviceBase):
    id: str
    is_online: bool = False
