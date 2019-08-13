from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class GroupItem(Base):
    __tablename__ = 'group_items'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship('Group', backref='group_items')
    item = relationship('Item', backref='group_items')
