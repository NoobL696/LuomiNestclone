from loguru import logger
from typing import Optional


class Router:
    async def route(self, intent: str) -> str:
        logger.debug(f"Router route: {intent}")
        return "companion"
