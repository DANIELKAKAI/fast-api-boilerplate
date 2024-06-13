import enum

from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from src.database import Base


class ItemStatusEnum(enum.Enum):
    NEW = "NEW"
    APPROVED = "APPROVED"
    EOL = "EOL"


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    status = Column(Enum(ItemStatusEnum), nullable=False, default="NEW")
    description = Column(String(50))
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")
    item_history = relationship("ItemHistory", back_populates="item")


class ItemHistory(Base):
    __tablename__ = "item_history"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    item = relationship("Item", back_populates="item_history")
    old_assignee_id = Column(Integer, ForeignKey("users.id"))
    old_assignee = relationship("User", foreign_keys=[old_assignee_id])
    new_assignee_id = Column(Integer, ForeignKey("users.id"))
    new_assignee = relationship("User", foreign_keys=[new_assignee_id])
    old_status = Column(Enum(ItemStatusEnum), nullable=False)
    new_status = Column(Enum(ItemStatusEnum), nullable=False)
