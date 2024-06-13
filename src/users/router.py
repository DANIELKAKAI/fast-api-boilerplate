from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.items.controllers import create_user_item, reassign_item
from src.items.schemas import ItemCreate, Item
from src.dependancies import get_db
from src.users.controllers import get_user_by_email, create_user
from src.users.schemas import User, UserCreate, UserId

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.post("/{user_id}/items/", response_model=Item)
def create_item_for_user(
    user_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    return create_user_item(db=db, item=item, user_id=user_id)


@router.post("/reassign_item/{item_id}/", response_model=Item)
def assign_item(
    item_id: int, new_owner: UserId, db: Session = Depends(get_db)
):
    return reassign_item(db=db, item_id=item_id, new_owner=new_owner)
