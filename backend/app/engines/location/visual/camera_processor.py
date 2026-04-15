from loguru import logger
from typing import Optional


class CameraProcessor:
    async def process(self, frame: bytes) -> Optional[dict]:
        logger.debug("CameraProcessor process stub")
        return None
