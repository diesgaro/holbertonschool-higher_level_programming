#!/usr/bin/python3
"""
    Task 6, create table with ORM-SQLALchemy
"""
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        Class State
    """
    __tablename__ = 'states'
    id = Column(Integer, Sequence('id'), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
