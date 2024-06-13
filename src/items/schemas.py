from pydantic import BaseModel
from typing import Optional, List


class ItemHistory(BaseModel):
    id: int
    old_assignee_id: int
    new_assignee_id: int
    old_status: str
    new_status: str

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    status: str
    item_history: List[ItemHistory] = []

    class Config:
        orm_mode = True


class Status(BaseModel):
    name: str
