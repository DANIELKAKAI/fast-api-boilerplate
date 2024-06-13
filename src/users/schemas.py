from typing import List

from pydantic import BaseModel

from src.items.schemas import Item


class UserId(BaseModel):
    id: int


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
