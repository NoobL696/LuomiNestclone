from loguru import logger
from typing import Optional


class MQTTClient:
    async def connect(self, broker: str, port: int = 1883) -> bool:
        logger.debug(f"MQTT connect: {broker}:{port}")
        return True

    async def publish(self, topic: str, payload: str) -> None:
        logger.debug(f"MQTT publish: {topic}")

    async def subscribe(self, topic: str) -> None:
        logger.debug(f"MQTT subscribe: {topic}")

    async def disconnect(self) -> None:
        logger.debug("MQTT disconnect")


_mqtt_client: Optional[MQTTClient] = None


async def init_mqtt() -> None:
    global _mqtt_client
    _mqtt_client = MQTTClient()
    logger.info("MQTT init stub")


async def close_mqtt() -> None:
    global _mqtt_client
    if _mqtt_client:
        await _mqtt_client.disconnect()
        _mqtt_client = None
    logger.info("MQTT close stub")
