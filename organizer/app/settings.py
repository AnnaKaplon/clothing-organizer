import os


class Config:
    """Flask application configuration"""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")

    SECRET_KEY = '\xbf\xde\xe1\xcf\xf0\xf8\x8b\x89\xc0\xbfjCR\xd8\x110&\x1d\x83\xf9T;\x9d\xd4'
