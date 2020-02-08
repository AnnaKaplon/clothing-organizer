import json
from typing import Optional

from flask import Blueprint, request, Response
from flask_login import LoginManager, login_user, logout_user, login_required
from marshmallow import ValidationError

from organizer.app.logging.schemas import LoggingSchema
from organizer.models.user import User
from organizer.utils.request import get_request_data


login_api = Blueprint('login', __name__)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: int) -> Optional[User]:
    return User.get_user_by_id(user_id)


@login_api.route('/login', methods=["POST"])
def login():
    serializer = LoggingSchema()

    try:
        serializer.load(get_request_data(request))
    except ValidationError as exc:
        return Response(response=json.dumps(exc.messages), status=400)

    login_user(serializer.context["user"])

    return Response(status=200)


@login_api.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return Response(status=200)
