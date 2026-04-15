from loguru import logger


class EmotionMapper:
    def map_emotion(self, emotion: str) -> dict:
        return {"expression": "neutral", "motion": "idle"}
