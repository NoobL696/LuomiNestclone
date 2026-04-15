from loguru import logger
from typing import List, Optional


class MCPToolRegistry:
    async def register(self, tool_name: str, description: str, schema: dict) -> None:
        logger.debug(f"MCPToolRegistry register: {tool_name}")

    async def list_tools(self) -> List[dict]:
        return []

    async def get_tool(self, tool_name: str) -> Optional[dict]:
        return None
