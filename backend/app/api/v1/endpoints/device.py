from fastapi import APIRouter

router = APIRouter(prefix="/devices", tags=["devices"])


@router.get("/")
async def list_devices():
    return {"devices": []}
