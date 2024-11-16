from sqlalchemy.ext.asyncio import AsyncSession
from backend.src.shemas.obligation import ObligationAct, ObligationUpdate
from sqlalchemy import select, update
from backend.src.database import models
from backend.src.exception.exc import NOT_FOUND


async def add_obligation(session: AsyncSession, schema: ObligationAct):
    event = await session.get(models.Event, schema.event)
    borrower = await session.get(models.User, schema.borrower)
    lender = await session.get(models.User, schema.lender)

    entity = models.Obligations(
        event=event.id,
        amount=schema.amount,
        borrower=borrower.id,
        lender=lender.id,
    )

    session.add(entity)
    await session.commit()
    await session.refresh(entity)
    return entity


async def update_obligation(session: AsyncSession, schema: ObligationUpdate):
    query = select(models.Obligations).where(
        models.Obligations.event == schema.event,
        models.Obligations.lender == schema.lender,
        models.Obligations.borrower == schema.borrower,
    )

    result = await session.execute(query)
    obligations = result.scalars().first()

    if not obligations:
        raise NOT_FOUND

    stmt = (
        update(models.Obligations)
        .where(
            models.Obligations.event == schema.event,
            models.Obligations.lender == schema.lender,
            models.Obligations.borrower == schema.borrower,
        )
        .values(amount=schema.amount)
    )

    result = await session.execute(stmt)
    await session.commit()
    return obligations


async def get_obligations(session: AsyncSession, event_id: int):
    query = select(models.Obligations).where(models.Obligations.event == event_id)
    result = await session.execute(query)
    return result.scalars().all()
