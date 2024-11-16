from pydantic import BaseModel


class Obligation(BaseModel):
    event: int


class ObligationAct(Obligation):
    lender: int
    borrower: int
    amount: int


class ObligationUpdate(Obligation):
    lender: int
    borrower: int
    amount: int
