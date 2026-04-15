from typing import Optional
from loguru import logger


async def s3_upload(bucket: str, key: str, data: bytes) -> str:
    logger.debug(f"S3 upload stub: {bucket}/{key}")
    return f"s3://{bucket}/{key}"


async def s3_download(bucket: str, key: str) -> Optional[bytes]:
    logger.debug(f"S3 download stub: {bucket}/{key}")
    return None
