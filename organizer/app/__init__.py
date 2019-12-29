from flask import Flask

from organizer.app.settings import Config
from organizer.app.logging import login_manager, login_api


def make_app() -> Flask:
    """Create Flask application"""
    application = Flask(__name__)
    application.config.from_object(Config())
    login_manager.init_app(application)
    register_blueprints(application)

    return application


def register_blueprints(app: Flask) -> None:
    """Register blueprints"""
    app.register_blueprint(login_api)
