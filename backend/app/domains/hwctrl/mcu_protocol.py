from loguru import logger
from typing import Optional


class MCUProtocol:
    async def send_command(self, command: str, params: dict = None) -> Optional[dict]:
        logger.debug(f"MCU command: {command}")
        return {"status": "ok"}

    async def read_state(self) -> dict:
        return {}
