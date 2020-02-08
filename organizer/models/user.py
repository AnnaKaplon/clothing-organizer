from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean

from organizer.models import Base


class User(Base, UserMixin):
    """User model definition"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    active = Column(Boolean, nullable=False, default=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def is_active(self) -> bool:
        return self.active
