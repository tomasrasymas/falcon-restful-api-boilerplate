from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .base import Base
from models.group_item import GroupItem


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50))

    groups = relationship('Group', backref='items', secondary=GroupItem.__table__)
