from pydantic import BaseModel
from typing import Optional


class PluginBase(BaseModel):
    name: str
    version: str = "1.0.0"
    description: Optional[str] = None


class PluginResponse(PluginBase):
    id: str
    is_enabled: bool = True
