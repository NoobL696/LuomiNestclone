from typing import AsyncGenerator


async def get_db_session() -> AsyncGenerator:
    yield None
