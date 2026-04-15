from loguru import logger
from typing import Optional


class ContextWindow:
    def __init__(self, max_tokens: int = 4096):
        self.max_tokens = max_tokens
        self._messages = []

    def add(self, role: str, content: str) -> None:
        self._messages.append({"role": role, "content": content})

    def get_context(self) -> list:
        return self._messages
