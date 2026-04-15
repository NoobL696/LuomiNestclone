from loguru import logger


class AIToAIChat:
    async def start_conversation(self, agent_a: str, agent_b: str, topic: str) -> dict:
        return {"status": "started"}

    async def get_conversation(self, conversation_id: str) -> dict:
        return {"messages": []}
