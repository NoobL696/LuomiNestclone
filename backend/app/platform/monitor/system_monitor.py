from loguru import logger


class SystemMonitor:
    async def get_cpu_usage(self) -> float:
        return 0.0

    async def get_memory_usage(self) -> float:
        return 0.0

    async def get_disk_usage(self) -> float:
        return 0.0
