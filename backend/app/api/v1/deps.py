from fastapi import Depends

async def get_current_user():
    return {"id": "default_user", "username": "default"}
