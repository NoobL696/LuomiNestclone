from loguru import logger
from typing import Optional


class VADDetector:
    async def detect(self, audio_data: bytes) -> bool:
        return False
