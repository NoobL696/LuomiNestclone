from loguru import logger


class Storyteller:
    async def tell_story(self, theme: str, style: str = "fairytale") -> str:
        logger.debug(f"Storyteller stub: {theme}")
        return ""
