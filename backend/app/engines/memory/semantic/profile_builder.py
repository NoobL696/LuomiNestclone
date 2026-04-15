from loguru import logger


class ProfileBuilder:
    async def build(self, user_id: str) -> dict:
        logger.debug(f"ProfileBuilder build: {user_id}")
        return {}
