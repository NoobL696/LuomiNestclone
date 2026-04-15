from loguru import logger
from typing import List


class ChunkStrategy:
    def chunk(self, text: str, max_size: int = 500) -> List[str]:
        return [text[i:i+max_size] for i in range(0, len(text), max_size)]
