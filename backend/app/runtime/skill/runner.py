from loguru import logger


class SkillRunner:
    async def run(self, skill_id: str, params: dict = None) -> dict:
        logger.debug(f"SkillRunner run: {skill_id}")
        return {"status": "completed"}
