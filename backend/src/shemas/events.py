from datetime import datetime
from pydantic import BaseModel


class Event(BaseModel):
    id: int
    created_at: datetime
    title: str
    link: str
    owner: int


class EventCreate(BaseModel):
    title: str
    owner: int


class EventUpdate(BaseModel):
    title: str


class AllEventUsers(BaseModel):
    users: list[int]


class Cheque(BaseModel):
    id: int
    params: str


class Obligations(BaseModel):
    lender: int
    borrower: int
    event: int
    amount: int
