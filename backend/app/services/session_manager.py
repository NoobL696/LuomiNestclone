from typing import Optional, List


class SessionManager:
    async def create_session(self, user_id: str) -> dict:
        return {"id": "stub", "user_id": user_id}

    async def get_session(self, session_id: str) -> Optional[dict]:
        return None

    async def list_sessions(self, user_id: str) -> List[dict]:
        return []
