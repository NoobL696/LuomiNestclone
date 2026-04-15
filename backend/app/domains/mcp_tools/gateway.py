from loguru import logger
from typing import List


class MCPGateway:
    async def list_servers(self) -> List[dict]:
        return []

    async def route_request(self, tool_name: str, arguments: dict) -> dict:
        logger.debug(f"MCPGateway route: {tool_name}")
        return {"status": "routed"}
