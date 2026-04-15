from loguru import logger
from typing import Optional


class WindowsAdapter:
    async def get_system_info(self) -> dict:
        return {"os": "windows", "version": "unknown"}

    async def run_command(self, command: str) -> Optional[str]:
        logger.debug(f"WindowsAdapter run_command: {command}")
        return None
