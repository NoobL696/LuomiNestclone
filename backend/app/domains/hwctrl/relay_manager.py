from loguru import logger


class RelayManager:
    async def turn_on(self, relay_id: str) -> None:
        logger.debug(f"Relay ON: {relay_id}")

    async def turn_off(self, relay_id: str) -> None:
        logger.debug(f"Relay OFF: {relay_id}")

    async def get_state(self, relay_id: str) -> bool:
        return False
