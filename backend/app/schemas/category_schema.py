from pydantic import BaseModel
from typing import Optional
import datetime

class CategoryBase(BaseModel):
    name: str
    type: str

class CategoryCreate(CategoryBase):
    user_id: int

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None

class CategoryResponse(CategoryBase):
    id: int
    user_id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True