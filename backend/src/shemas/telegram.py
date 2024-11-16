from pydantic import BaseModel


class TelegramUser(BaseModel):
    tg_id: int
    amount: int
