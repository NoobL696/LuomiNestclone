from loguru import logger
from typing import Optional


class DatabaseManager:
    async def init(self) -> None:
        logger.debug("DatabaseManager init stub")

    async def close(self) -> None:
        logger.debug("DatabaseManager close stub")

    async def get_session(self):
        return None
