from pydantic import BaseModel
from typing import Optional
import datetime
from decimal import Decimal

class AccountBase(BaseModel):
    name: str
    type: str
    user_id: int

class AccountCreate(AccountBase):
    balance: Optional[Decimal] = None

class AccountUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    balance: Optional[Decimal] = None

class AccountResponse(BaseModel):
    id: int
    name: str
    type: str
    user_id: int
    balance: Decimal
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True