from loguru import logger
from typing import Optional


class MCPClient:
    async def connect(self, server_url: str) -> bool:
        logger.debug(f"MCP connect: {server_url}")
        return True

    async def call_tool(self, tool_name: str, arguments: dict) -> Optional[dict]:
        return None
