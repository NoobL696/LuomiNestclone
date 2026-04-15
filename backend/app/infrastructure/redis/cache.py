from typing import Any, Optional


async def get_cache(key: str) -> Optional[str]:
    return None


async def set_cache(key: str, value: str, ttl: int = 300) -> None:
    pass


async def delete_cache(key: str) -> None:
    pass
