from loguru import logger
from typing import Optional


async def init_redis() -> None:
    logger.info("Redis init stub")


async def close_redis() -> None:
    logger.info("Redis close stub")
