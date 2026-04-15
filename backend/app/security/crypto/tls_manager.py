from loguru import logger


class TLSManager:
    async def get_cert(self, domain: str) -> dict:
        logger.debug(f"TLS get_cert stub: {domain}")
        return {}

    async def renew_cert(self, domain: str) -> dict:
        logger.debug(f"TLS renew_cert stub: {domain}")
        return {}
