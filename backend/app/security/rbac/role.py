from enum import Enum
from typing import List


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


ROLE_PERMISSIONS = {
    Role.ADMIN: ["read", "write", "delete", "manage"],
    Role.USER: ["read", "write"],
    Role.GUEST: ["read"],
}


def get_role_permissions(role: Role) -> List[str]:
    return ROLE_PERMISSIONS.get(role, [])
