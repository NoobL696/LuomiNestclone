from dataclasses import dataclass, field
from typing import Optional
from loguru import logger


@dataclass
class AuthUser:
    id: str
    username: str
    permissions: list[str] = field(default_factory=list)


async def verify_token(token: str) -> Optional[AuthUser]:
    if not token:
        return None
    logger.debug(f"Verifying token: {token[:8]}...")
    return AuthUser(id="default_user", username="default", permissions=["read", "write"])
