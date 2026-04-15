from loguru import logger


class WakeWordDetector:
    async def detect(self, audio_data: bytes) -> bool:
        return False

    async def add_wake_word(self, word: str) -> None:
        logger.debug(f"WakeWord add: {word}")
