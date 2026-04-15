from loguru import logger
from typing import Optional


class ModelLoader:
    async def load(self, model_path: str) -> Optional[dict]:
        logger.debug(f"ModelLoader load: {model_path}")
        return None
