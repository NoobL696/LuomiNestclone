from fastapi import WebSocket
from app.api.ws.manager import manager
from loguru import logger


async def handle_websocket(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            logger.debug(f"WS received from {client_id}: {data}")
    except Exception:
        manager.disconnect(client_id)
