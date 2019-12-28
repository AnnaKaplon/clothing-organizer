from marshmallow import Schema
from marshmallow.utils import EXCLUDE


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE
