from loguru import logger


class DockerAdapter:
    async def get_containers(self) -> list:
        return []

    async def run_container(self, image: str, **kwargs) -> dict:
        logger.debug(f"DockerAdapter run: {image}")
        return {"status": "running"}
