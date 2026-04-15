from loguru import logger
from typing import Optional


class VRMLoader:
    async def load(self, model_path: str) -> Optional[dict]:
        logger.debug(f"VRMLoader load: {model_path}")
        return None
