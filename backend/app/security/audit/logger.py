from loguru import logger
from datetime import datetime
from typing import Any, Optional


class AuditLogger:
    async def log(self, action: str, user_id: str, resource: str = "", details: Optional[dict] = None) -> None:
        logger.info(f"AUDIT: {action} by {user_id} on {resource} - {details or {}}")

    async def query(self, user_id: Optional[str] = None, action: Optional[str] = None) -> list:
        return []


audit_logger = AuditLogger()
