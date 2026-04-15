from fastapi import APIRouter

router = APIRouter(prefix="/mcp", tags=["mcp"])


@router.get("/")
async def list_mcp_tools():
    return {"tools": []}
