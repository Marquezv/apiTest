from pydantic import BaseModel
from typing import Optional

class SimpleUser(BaseModel):
    id: Optional[int] = None
    name: str
    status: bool
    class Config:
        orm_mode = True

class User(BaseModel):
    id: Optional[int] = None
    name: str
    password: str
    class Config:
        orm_mode = True

class LoginData(BaseModel):
    name: str
    password: str

class LoginSucess(BaseModel):
    user: SimpleUser
    access_token: str
