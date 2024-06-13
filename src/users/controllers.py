import os

from sqlalchemy.orm import Session


from dotenv import load_dotenv

from src.users.models import User
from src.users.schemas import UserCreate


load_dotenv()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + os.getenv("PASSWORD_HASH")
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
