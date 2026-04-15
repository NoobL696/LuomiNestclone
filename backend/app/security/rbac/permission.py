from typing import List
from app.security.rbac.role import Role, get_role_permissions


def check_permission(role: Role, required: str) -> bool:
    permissions = get_role_permissions(role)
    return required in permissions


def require_permissions(*perms: str):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)
        return wrapper
    return decorator
