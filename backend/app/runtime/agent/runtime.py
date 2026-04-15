from loguru import logger
from typing import Optional


class AgentRuntime:
    async def start(self, agent_id: str) -> bool:
        logger.debug(f"AgentRuntime start: {agent_id}")
        return True

    async def stop(self, agent_id: str) -> None:
        logger.debug(f"AgentRuntime stop: {agent_id}")
