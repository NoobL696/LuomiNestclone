from loguru import logger


class MotionPlayer:
    async def play(self, motion_name: str) -> None:
        logger.debug(f"MotionPlayer play: {motion_name}")
