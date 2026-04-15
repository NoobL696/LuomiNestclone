from loguru import logger


class EdgeEngine:
    async def synthesize(self, text: str, voice: str = "zh-CN-XiaoxiaoNeural") -> bytes:
        logger.debug("EdgeEngine synthesize stub")
        return b""
