from fastapi import APIRouter

router = APIRouter(prefix="/avatars", tags=["avatars"])


@router.get("/")
async def list_avatars():
    return {"avatars": []}
