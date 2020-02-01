from typing import Optional

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean

from organizer.models import Base, session
from organizer.utils.crypt import password_crypter


class User(Base, UserMixin):
    """User model definition"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    active = Column(Boolean, nullable=False, default=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def is_active(self) -> bool:
        return self.active

    @classmethod
    def create_user(cls, email: str, password: str) -> None:
        """
        Create new user with given email and password.

        Password is hashed using pbkdf2_sha256 hash.
        """
        user = User()
        user.email = email
        user.password = password_crypter.hash(password)

        session.add(user)

    @classmethod
    def get_user_by_id(cls, user_id: int) -> Optional["User"]:
        """Return user with given id or None if no such user found."""
        return session.query(User).filter(User.id == user_id).first()

    @classmethod
    def get_user_by_email(cls, email: str) -> Optional["User"]:
        """Retrun user with given email or None if no such user found."""
        return session.query(User).filter(User.email == email).first()
