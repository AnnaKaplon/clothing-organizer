from sqlalchemy import Column, Integer, String, UniqueConstraint

from organizer.dal.db import Base


class User(Base):
    """User model definition"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
