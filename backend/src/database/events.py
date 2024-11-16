from fastapi import FastAPI
from backend.src.database.models import User, Event, Obligations, Cheque
from backend.src.database.db import engine
from sqlalchemy.ext.asyncio import AsyncEngine


async def init_db_tables(conn: AsyncEngine) -> None:
    await conn.run_sync(User.metadata.drop_all)
    await conn.run_sync(User.metadata.create_all)
    await conn.run_sync(Event.metadata.drop_all)
    await conn.run_sync(Event.metadata.create_all)
    await conn.run_sync(Obligations.metadata.drop_all)
    await conn.run_sync(Obligations.metadata.create_all)
    await conn.run_sync(Cheque.metadata.drop_all)
    await conn.run_sync(Cheque.metadata.create_all)


async def init_db_connection(backend_app: FastAPI) -> None:
    async with engine.begin() as connection:
        await init_db_tables(connection)