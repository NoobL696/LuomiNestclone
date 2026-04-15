from loguru import logger


class CubismCore:
    async def initialize(self, model_path: str) -> bool:
        logger.debug(f"CubismCore init: {model_path}")
        return True
