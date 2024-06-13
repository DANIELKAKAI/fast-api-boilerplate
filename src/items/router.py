from typing import Optional

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.items.schemas import Item, Status
from src.items.controllers import (
    list_items,
    get_item_by_id,
    change_item_status,
)
from src.dependancies import get_db

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[Item])
def read_items(status: Optional[str] = None, db: Session = Depends(get_db)):
    return list_items(db=db, status=status)


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db=db, item_id=item_id)


@router.post("/status/{item_id}/", response_model=Item)
def assign_item(item_id: int, status: Status, db: Session = Depends(get_db)):
    return change_item_status(db=db, item_id=item_id, status=status)
