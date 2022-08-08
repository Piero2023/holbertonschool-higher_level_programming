#!/usr/bin/python3
""" This script lists all State objects with the name passed as
argument from database hbtn_0e_6_usa """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    is the class City inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
