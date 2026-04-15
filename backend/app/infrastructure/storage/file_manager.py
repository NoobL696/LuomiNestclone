from typing import Optional
from loguru import logger
import os


class FileManager:
    async def read(self, path: str) -> Optional[bytes]:
        if not os.path.exists(path):
            return None
        with open(path, "rb") as f:
            return f.read()

    async def write(self, path: str, data: bytes) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(data)

    async def delete(self, path: str) -> bool:
        if os.path.exists(path):
            os.remove(path)
            return True
        return False

    async def exists(self, path: str) -> bool:
        return os.path.exists(path)


file_manager = FileManager()
