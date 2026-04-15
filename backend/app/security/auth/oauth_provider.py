from typing import Optional
from loguru import logger


class OAuthProvider:
    async def authenticate(self, provider: str, code: str) -> Optional[dict]:
        logger.debug(f"OAuth authenticate stub: {provider}")
        return None
