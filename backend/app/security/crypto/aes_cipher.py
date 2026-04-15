from cryptography.fernet import Fernet
from app.core.config import settings
from loguru import logger


class AESCipher:
    def __init__(self):
        self._key = Fernet.generate_key()
        self._cipher = Fernet(self._key)

    def encrypt(self, data: str) -> str:
        return self._cipher.encrypt(data.encode()).decode()

    def decrypt(self, encrypted: str) -> str:
        return self._cipher.decrypt(encrypted.encode()).decode()


aes_cipher = AESCipher()
