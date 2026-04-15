from loguru import logger


class SyncService:
    async def sync(self, source: str, target: str) -> dict:
        logger.debug(f"SyncService: {source} -> {target}")
        return {"status": "synced"}
