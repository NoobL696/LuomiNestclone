from fastapi import APIRouter
from typing import Optional

router = APIRouter(prefix="/skills", tags=["skills"])


@router.get("/")
async def list_skills(category: Optional[str] = None, source: Optional[str] = None):
    return {"skills": [], "total": 0}


@router.get("/{skill_id}")
async def get_skill(skill_id: str):
    return {"id": skill_id, "name": "Unknown", "status": "available"}


@router.post("/install")
async def install_skill():
    return {"status": "installing"}


@router.post("/upload")
async def upload_skill():
    return {"status": "uploaded"}


@router.delete("/{skill_id}")
async def uninstall_skill(skill_id: str):
    return {"status": "uninstalled"}
