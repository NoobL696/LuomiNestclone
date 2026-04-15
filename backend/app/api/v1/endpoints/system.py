from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["system"])


@router.get("/info")
async def system_info():
    return {"name": "LuomiNest", "version": "0.1.0", "status": "running"}
