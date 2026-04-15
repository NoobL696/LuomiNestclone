from loguru import logger


class PreferenceLearner:
    async def learn(self, user_id: str, interaction: dict) -> None:
        logger.debug(f"PreferenceLearner: {user_id}")

    async def get_preferences(self, user_id: str) -> dict:
        return {}
