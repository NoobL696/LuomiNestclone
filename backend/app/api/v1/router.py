from fastapi import APIRouter
from app.api.v1.endpoints import (
    agent, avatar, chat, device, iot, mcp, memory,
    plugin, session, skill, social, system, user,
)

api_router = APIRouter()

api_router.include_router(agent.router)
api_router.include_router(avatar.router)
api_router.include_router(chat.router)
api_router.include_router(device.router)
api_router.include_router(iot.router)
api_router.include_router(mcp.router)
api_router.include_router(memory.router)
api_router.include_router(plugin.router)
api_router.include_router(session.router)
api_router.include_router(skill.router)
api_router.include_router(social.router)
api_router.include_router(system.router)
api_router.include_router(user.router)


@api_router.get("/health")
async def health_check():
    return {"status": "ok", "version": "0.1.0"}
