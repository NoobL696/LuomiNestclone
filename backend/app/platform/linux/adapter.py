from loguru import logger
from typing import Optional


class LinuxAdapter:
    async def get_system_info(self) -> dict:
        return {"os": "linux", "version": "unknown"}

    async def run_command(self, command: str) -> Optional[str]:
        logger.debug(f"LinuxAdapter run_command: {command}")
        return None
