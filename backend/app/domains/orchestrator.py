from loguru import logger
from typing import Any


class Orchestrator:
    def __init__(self):
        self._agents = {}

    async def dispatch(self, intent: str, context: dict) -> dict:
        logger.debug(f"Orchestrator dispatch: {intent}")
        return {"response": "ok", "intent": intent}
