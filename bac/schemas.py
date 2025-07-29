from pydantic import BaseModel
from typing import Optional

class TransactionBase(BaseModel):
    amount: int
    category: str
    description: Optional[str] = ""
    date: str
    is_income: bool

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    id: int

    class Config:
        orm_mode = True
