from pydantic import BaseModel
from typing import Optional

class Test(BaseModel):
    name: str
    age: int
    phone: Optional[str] = None
