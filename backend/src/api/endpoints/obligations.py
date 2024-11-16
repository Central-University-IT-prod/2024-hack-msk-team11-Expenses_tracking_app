from fastapi import APIRouter
from starlette import status
from backend.src.crud import obligations as crud_obligations
from backend.src.exception.exc import NOT_FOUND
from backend.src.shemas.obligation import ObligationAct, ObligationUpdate
from backend.src.api.dep import CurrentSessionDep

router = APIRouter(prefix="/obligations", tags=["obligation"])


@router.get(
    path="/all/{event_id}",
    status_code=status.HTTP_200_OK,
    response_model=list[ObligationAct],
)
async def get_all_obligations(event_id: int, session: CurrentSessionDep):
    obligations = await crud_obligations.get_obligations(
        event_id=event_id,
        session=session,
    )
    if not obligations:
        raise NOT_FOUND

    return obligations


@router.post(path="/add", status_code=status.HTTP_201_CREATED)
async def create_obligation(schema: ObligationAct, session: CurrentSessionDep):
    obligation = await crud_obligations.add_obligation(session=session, schema=schema)
    return obligation


@router.put(path="/", status_code=status.HTTP_200_OK)
async def update_obligation(schema: ObligationUpdate, session: CurrentSessionDep):
    obligation = await crud_obligations.update_obligation(schema=schema, session=session)
    return obligation
