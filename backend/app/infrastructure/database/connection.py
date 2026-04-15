from loguru import logger
from typing import Optional


async def init_db() -> None:
    logger.info("Database init stub")


async def close_db() -> None:
    logger.info("Database close stub")
