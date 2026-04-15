from loguru import logger
from typing import Optional


class ImageAnalyzer:
    async def analyze(self, image_data: bytes, prompt: str = "") -> dict:
        logger.debug("ImageAnalyzer analyze stub")
        return {"description": ""}
