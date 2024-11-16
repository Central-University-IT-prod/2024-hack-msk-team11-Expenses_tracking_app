from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.src.database.db import get_async_session

CurrentSessionDep = Annotated[AsyncSession, Depends(get_async_session)]
