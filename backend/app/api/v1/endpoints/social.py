from fastapi import APIRouter

router = APIRouter(prefix="/social", tags=["social"])


@router.get("/")
async def list_social_contacts():
    return {"contacts": []}
