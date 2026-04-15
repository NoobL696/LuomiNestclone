from fastapi import APIRouter

router = APIRouter(prefix="/iot", tags=["iot"])


@router.get("/")
async def list_iot_devices():
    return {"devices": []}
