from loguru import logger


class WhisperProvider:
    provider_name: str = "whisper"

    async def transcribe(self, audio_data: bytes, **kwargs) -> str:
        logger.debug("Whisper provider stub")
        return ""
