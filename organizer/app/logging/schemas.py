from marshmallow import fields, validates_schema, ValidationError

from organizer.bl.user import get_user_by_email
from organizer.utils.crypt import password_crypter
from organizer.utils.schemas import BaseSchema


class LoggingSchema(BaseSchema):
    email = fields.Email(required=True)
    password = fields.String(required=True)

    @validates_schema
    def validate_credentials(self, data, **kwargs):
        """Validate correctness of passed credentials."""
        user = get_user_by_email(data["email"])

        if not user or not password_crypter.verify(data["password"], user.password):
            raise ValidationError("Incorrect credentials")

        self.context["user"] = user
