from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    role: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TenderCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TenderRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    date_uploaded: datetime

    class Config:
        orm_mode = True
