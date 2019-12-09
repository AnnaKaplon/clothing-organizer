from flask import Flask

from organizer.app.settings import Config


def make_app():
    application = Flask(__name__)
    application.config.from_object(Config())

    return application
