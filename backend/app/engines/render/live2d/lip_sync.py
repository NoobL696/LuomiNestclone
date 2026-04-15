from loguru import logger


class LipSync:
    async def sync(self, audio_data: bytes) -> dict:
        return {"mouth_open": 0.0}
