from fastapi import APIRouter
from backend.src.shemas import users, events
from backend.src.exception import exc
from backend.src.crud import users as crud_users
from backend.src.api.dep import CurrentSessionDep


router = APIRouter(prefix="/pinguins", tags=["authentification"])


@router.get(
    path="/{user_id}",
    response_model=users.User,
)
async def get_user(user_id: int):
    user = await crud_users.get_by_id(id=user_id, session=CurrentSessionDep)
    if not user:
        raise exc.HTTPException(
            status_code=404, detail=f"User with email {user.username} does not exist"
        )


@router.post(
    path="/",
    status_code=201,
)
async def create_user(user: users.User, session: CurrentSessionDep):
    await crud_users.create_user(schema=user, session=session)


@router.get(
    path="/{user_id}/events",
    response_model=list[events.Event],
)
async def get_user_events(user_id: int, session: CurrentSessionDep):
    events = await crud_users.get_user_events(
        user_id=user_id,
        session=session,
    )
    
    return events