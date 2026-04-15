from typing import Callable, Optional


class TopicManager:
    def __init__(self):
        self._topics: dict[str, str] = {}

    def register(self, name: str, topic: str) -> None:
        self._topics[name] = topic

    def get(self, name: str) -> Optional[str]:
        return self._topics.get(name)


topic_manager = TopicManager()
