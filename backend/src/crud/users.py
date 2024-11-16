from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.src.database import models
from backend.src.shemas import users


async def get_by_id(id: int, session: AsyncSession):
    stmt = select(models.User).where(models.User.id == id)
    result = await session.execute(stmt)
    return result.scalar()


async def create_user(schema: users.User, session: AsyncSession):
    user = await session.get(entity=models.User, ident=schema.id)
    if user:
        return

    user = models.User(id=schema.id)

    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def get_user_events(user_id: int, session: AsyncSession):
    user = await session.get(models.User, user_id)

    await session.refresh(user)
    return user.events
