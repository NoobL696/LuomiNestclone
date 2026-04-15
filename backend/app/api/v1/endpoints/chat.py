from fastapi import APIRouter

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/")
async def create_chat():
    return {"message": "Chat endpoint (stub)"}
