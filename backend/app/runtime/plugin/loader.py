from loguru import logger
from typing import Optional


class PluginLoader:
    async def load(self, plugin_path: str) -> Optional[dict]:
        logger.debug(f"PluginLoader load: {plugin_path}")
        return None

    async def unload(self, plugin_id: str) -> None:
        logger.debug(f"PluginLoader unload: {plugin_id}")
