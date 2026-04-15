from loguru import logger


class DialogueManager:
    async def generate_response(self, context: dict) -> str:
        logger.debug("DialogueManager generate_response stub")
        return "你好，我是洛米！"
