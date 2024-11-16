from datetime import datetime

import secrets

from fastapi import HTTPException
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from backend.src.database import models
from backend.src.shemas import events, users


async def get_by_id(event_id: int, session: AsyncSession):
    stmt = select(models.Event).where(models.Event.id == event_id)
    result = await session.execute(stmt)
    return result.scalar()


async def get_by_link(link: str, session: AsyncSession):
    stmt = select(models.Event).where(models.Event.link == link)
    result = await session.execute(stmt)
    return result.scalar()


async def get_all_users(event_id: int, session: AsyncSession):
    stmt = (
        select(models.User.id)
        .join(models.association_table)
        .join(models.Event)
        .where(models.Event.id == event_id)
        .distinct()
    )
    result = await session.execute(stmt)
    user_ids = result.scalars().all()

    return user_ids


async def create_event(schema: events.EventCreate, session: AsyncSession):
    owner = await session.get(models.User, schema.owner)
    
    if owner is None:
        owner = models.User(id=schema.owner)
        session.add(owner)
        await session.flush()
    

    entity = models.Event(
        title=schema.title,
        created_at=datetime.now(),
        link=secrets.token_urlsafe(16),
        owner=owner.id,
    )
    
    entity.users.append(owner)


    session.add(entity)
    await session.commit()
    await session.refresh(entity)
    return entity


async def update_event(
    event_id: int, schema: events.EventUpdate, session: AsyncSession
):
    query = select(models.Event).where(models.Event.id == event_id)

    result = await session.execute(query)
    event = result.scalars().first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    stmt = (
        update(models.Event)
        .where(models.Event.id == event_id)
        .values(title=schema.title)
    )

    result = await session.execute(stmt)
    await session.commit()
    return event


async def add_people(event_id: int, schema: users.User, session: AsyncSession):
    event = await session.get(models.Event, event_id)
    user = await session.get(models.User, schema.id)
    
    await session.refresh(event)

    # Проверяем, что пользователь еще не добавлен в событие
    if user.id not in [u.id for u in event.users]:
        event.users.append(user)
        await session.flush()  # Зафиксируем изменения в сессии перед коммитом
        await session.commit()
