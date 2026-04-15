from typing import Optional, List


class PluginService:
    async def list_plugins(self) -> List[dict]:
        return []

    async def get_plugin(self, plugin_id: str) -> Optional[dict]:
        return None

    async def install_plugin(self, source: str) -> dict:
        return {"status": "installing"}
