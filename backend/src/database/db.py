from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker
)

from backend.src.database.config import settings

engine = create_async_engine(settings.database_url)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session