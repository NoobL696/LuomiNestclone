from loguru import logger


class WhisperEngine:
    async def transcribe(self, audio_data: bytes, language: str = "zh") -> str:
        logger.debug("WhisperEngine transcribe stub")
        return ""
