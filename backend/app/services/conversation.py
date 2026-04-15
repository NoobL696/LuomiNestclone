from typing import Optional, List


class ConversationService:
    async def create_conversation(self, user_id: str, agent_id: str) -> dict:
        return {"id": "stub", "user_id": user_id, "agent_id": agent_id}

    async def get_conversation(self, conversation_id: str) -> Optional[dict]:
        return None

    async def list_conversations(self, user_id: str) -> List[dict]:
        return []
