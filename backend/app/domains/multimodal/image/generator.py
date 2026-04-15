from loguru import logger


class ImageGenerator:
    async def generate(self, prompt: str, size: str = "512x512") -> bytes:
        logger.debug(f"ImageGenerator stub: {prompt}")
        return b""
