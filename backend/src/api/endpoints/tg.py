from fastapi import status, APIRouter
from backend.src.shemas import telegram
from backend.src.exception.exc import BAD_REQUEST
from backend.src.bot import notify

router = APIRouter(prefix="/telegram", tags=["telegram_bot"])


@router.post("/bot", status_code=status.HTTP_201_CREATED)
async def bot(schema: telegram.TelegramUser):
    tg_id = schema.tg_id
    amount = schema.amount
    if not tg_id or not amount:
        raise BAD_REQUEST
    await notify(tg_id, amount)
    return
