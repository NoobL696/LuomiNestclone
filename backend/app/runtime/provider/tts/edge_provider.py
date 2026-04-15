from loguru import logger


class EdgeProvider:
    provider_name: str = "edge"

    async def synthesize(self, text: str, **kwargs) -> bytes:
        logger.debug("Edge TTS provider stub")
        return b""
