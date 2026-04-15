from app.infrastructure.mqtt.client import mqtt_client
from loguru import logger


async def publish(topic: str, payload: str, qos: int = 0) -> None:
    await mqtt_client.publish(topic, payload, qos)
