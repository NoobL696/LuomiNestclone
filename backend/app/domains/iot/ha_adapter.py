from loguru import logger


class HAAdapter:
    async def get_entity_state(self, entity_id: str) -> dict:
        return {"entity_id": entity_id, "state": "unknown"}

    async def call_service(self, domain: str, service: str, data: dict = None) -> dict:
        logger.debug(f"HA call_service: {domain}.{service}")
        return {"status": "ok"}
