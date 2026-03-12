from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime
from decimal import Decimal

class TransactionBase(BaseModel):
    user_id: int
    account_id: int
    category_id: int

class TransactionCreate(TransactionBase):
    amount: Decimal
    date: datetime.datetime
    description: Optional[str] = None

class TransactionUpdate(BaseModel):
    id: int
    amount: Optional[Decimal] = None
    date: Optional[str] = None
    account_id: Optional[int] = None
    description: Optional[str] = None
    category_id: Optional[int] = None

class TransactionResponse(BaseModel):
    id: int
    user_id: int
    account_id: Optional[int] = None
    category_id: Optional[int] = None
    amount: Optional[Decimal] = None
    date: Optional[datetime.datetime] = None
    description: Optional[str] = None
    created_at: datetime.datetime
    updated_at: Optional[datetime.datetime] = None

    model_config = ConfigDict(from_attributes=True)