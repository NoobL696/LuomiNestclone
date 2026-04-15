from loguru import logger


class AudioProcessor:
    async def process(self, audio_data: bytes) -> bytes:
        return audio_data

    async def normalize(self, audio_data: bytes) -> bytes:
        return audio_data
