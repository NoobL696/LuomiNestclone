from loguru import logger
from typing import Optional


class ProviderFactory:
    _providers = {}

    @classmethod
    def register(cls, name: str, provider_class):
        cls._providers[name] = provider_class

    @classmethod
    def create(cls, name: str, **kwargs):
        provider_class = cls._providers.get(name)
        if provider_class:
            return provider_class(**kwargs)
        logger.warning(f"Provider not found: {name}")
        return None
