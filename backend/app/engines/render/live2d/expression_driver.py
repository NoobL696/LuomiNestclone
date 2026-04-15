from loguru import logger


class ExpressionDriver:
    async def set_expression(self, expression: str) -> None:
        logger.debug(f"ExpressionDriver: {expression}")
