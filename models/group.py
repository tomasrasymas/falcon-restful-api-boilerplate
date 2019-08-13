from sqlalchemy import Column, String, Integer
from .base import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50))
    description = Column(String(length=500))
