from loguru import logger


class IntentClassifier:
    INTENT_MAP = {
        "chat": ["聊天", "说话", "对话", "talk", "chat"],
        "iot": ["开灯", "关灯", "温度", "空调", "设备"],
        "knowledge": ["查询", "搜索", "知道", "什么"],
        "creative": ["写", "画", "创作", "生成"],
        "social": ["发消息", "联系", "通知"],
    }

    async def classify(self, text: str) -> str:
        text_lower = text.lower()
        for intent, keywords in self.INTENT_MAP.items():
            for kw in keywords:
                if kw in text_lower:
                    logger.debug(f"Intent classified as [{intent}] for: {text}")
                    return intent
        return "chat"

    def select_agent(self, intent: str) -> str:
        agent_map = {
            "chat": "companion",
            "iot": "iot_controller",
            "knowledge": "knowledge_base",
            "creative": "creative_assistant",
            "social": "social_manager",
        }
        return agent_map.get(intent, "companion")
