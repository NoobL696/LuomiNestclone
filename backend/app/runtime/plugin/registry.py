from loguru import logger
from typing import List


class PluginRegistry:
    _plugins = {}

    @classmethod
    def register(cls, plugin_id: str, plugin):
        cls._plugins[plugin_id] = plugin

    @classmethod
    def get(cls, plugin_id: str):
        return cls._plugins.get(plugin_id)

    @classmethod
    def list_all(cls) -> List[str]:
        return list(cls._plugins.keys())
