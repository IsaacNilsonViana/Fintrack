from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    phone: Optional[str] = None
    password: str
    
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None
    created_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)
