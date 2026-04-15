from loguru import logger


class GPIOController:
    async def set_pin(self, pin: int, value: bool) -> None:
        logger.debug(f"GPIO set pin {pin} to {value}")

    async def get_pin(self, pin: int) -> bool:
        return False
