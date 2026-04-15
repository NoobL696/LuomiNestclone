from typing import Any, Optional, List


class SkillService:
    async def list_skills(self, category: Optional[str] = None, source: Optional[str] = None) -> List[dict]:
        return []

    async def get_skill(self, skill_id: str) -> Optional[dict]:
        return None

    async def install_skill(self, config: dict) -> dict:
        return {"status": "installing"}

    async def uninstall_skill(self, skill_id: str) -> dict:
        return {"status": "uninstalled"}

    async def upload_skill(self, file_path: str) -> dict:
        return {"status": "uploaded"}


skill_service = SkillService()
