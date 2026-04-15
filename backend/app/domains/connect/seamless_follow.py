from loguru import logger


class SeamlessFollow:
    async def follow(self, user_id: str, target_device: str) -> dict:
        logger.debug(f"SeamlessFollow: {user_id} -> {target_device}")
        return {"status": "following"}
