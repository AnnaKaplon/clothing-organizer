from typing import Optional

from sqlalchemy.orm.exc import NoResultFound

from organizer.dal.db import session
from organizer.dal.model.user import User
from organizer.utils.crypt import password_crypter


def create_user(email: str, password: str) -> None:
    """
    Create new user with given email and password.

    Password is hashed using pbkdf2_sha256 hash.
    """
    user = User()
    user.email = email
    user.password = password_crypter.hash(password)

    session.add(user)
    session.commit()


def get_user_by_id(user_id: int) -> Optional[User]:
    """Return user with given id or None if no such user found."""
    return session.query(User).filter(User.id == user_id).first()


def get_user_by_email(email: str) -> Optional[User]:
    """Retrun user with given email or None if no such user found."""
    return session.query(User).filter(User.email == email).first()
