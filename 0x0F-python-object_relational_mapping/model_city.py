#!/usr/bin/python3
"""
    Task 14, create model city with ORM-SQLALchemy
"""
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from model_state import Base


class City(Base):
    """
        Class City
    """
    __tablename__ = 'cities'
    id = Column(Integer, Sequence('id'), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
