from loguru import logger
from typing import Optional
from datetime import datetime


class AuditExporter:
    async def export_json(self, start: datetime, end: datetime, user_id: Optional[str] = None) -> str:
        logger.debug("Audit export JSON stub")
        return "[]"

    async def export_csv(self, start: datetime, end: datetime, user_id: Optional[str] = None) -> str:
        logger.debug("Audit export CSV stub")
        return ""
