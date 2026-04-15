from loguru import logger
from typing import Optional


class RedisManager:
    def __init__(self):
        self._data = {}

    async def get(self, key: str) -> Optional[str]:
        return self._data.get(key)

    async def set(self, key: str, value: str, expire: int = None) -> None:
        self._data[key] = value

    async def delete(self, key: str) -> None:
        self._data.pop(key, None)

    async def publish(self, channel: str, message: str) -> None:
        logger.debug(f"Redis publish: {channel}")

    async def subscribe(self, channel: str) -> None:
        logger.debug(f"Redis subscribe: {channel}")
