from typing import Any, Optional


async def get_state(key: str) -> Optional[dict]:
    return None


async def set_state(key: str, value: dict, ttl: int = 0) -> None:
    pass


async def delete_state(key: str) -> None:
    pass
