from loguru import logger


class OllamaProvider:
    provider_name: str = "ollama"

    async def chat(self, messages: list, **kwargs) -> str:
        logger.debug("Ollama chat stub")
        return ""
