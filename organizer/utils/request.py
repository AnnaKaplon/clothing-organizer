import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flask import Request


def get_request_data(request: "Request") -> dict:
    return json.loads(request.data)
