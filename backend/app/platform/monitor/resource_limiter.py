from loguru import logger


class ResourceLimiter:
    async def set_limit(self, resource: str, limit: float) -> None:
        logger.debug(f"ResourceLimiter set: {resource}={limit}")

    async def check_limit(self, resource: str) -> bool:
        return True
