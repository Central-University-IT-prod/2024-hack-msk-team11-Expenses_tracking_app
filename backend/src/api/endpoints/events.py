from fastapi import APIRouter, status, HTTPException

from backend.src.shemas import events, users
from backend.src.crud import events as crud_events
from backend.src.api.dep import CurrentSessionDep

router = APIRouter(prefix="/events", tags=["events"])


@router.get(
    path="/get_by_id/{event_id}",
    response_model=events.Event,
)
async def get_event_by_id(event_id: int, session: CurrentSessionDep):
    event = await crud_events.get_by_id(event_id=event_id, session=session)
    
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return event


@router.get(
    path="/get_by_link/{event_link}",
    response_model=events.Event,
)
async def get_event_by_link(event_link: str, session: CurrentSessionDep):
    event = await crud_events.get_by_link(link=event_link, session=session)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)   
    return event


@router.get(
    path="/{event_id}/users",
    response_model=events.AllEventUsers,
)
async def get_event_users(event_id: int, session: CurrentSessionDep):
    users = await crud_events.get_all_users(event_id=event_id, session=session)
    return {"users": users}


@router.post(
    path="/",
    response_model=events.Event,
    status_code=status.HTTP_201_CREATED,
)
async def create_event(event: events.EventCreate, session: CurrentSessionDep):
    event = await crud_events.create_event(event, session=session)
    return event


@router.put(
    path="/{event_id}",
)
async def update_event(event_id: int, event: events.EventUpdate, session: CurrentSessionDep):
    event = await crud_events.update_event(event_id, event, session=session)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    
@router.post(
    path="/{event_id}/add_people",
    status_code=status.HTTP_201_CREATED,
)
async def add_people(event_id: int, user: users.User, session: CurrentSessionDep):
    await crud_events.add_people(event_id=event_id, schema=user, session=session)