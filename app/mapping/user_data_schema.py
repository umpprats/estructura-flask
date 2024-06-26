from app.models import UserData
from marshmallow import fields, Schema, post_load

class UserDataSchema(Schema):
    id = fields.Integer(dump_only=True)
    firstname = fields.String(required=True, validate=fields.Length(min=1, max=80))
    lastname = fields.String(required=True, validate=fields.Length(min=1, max=80))
    address = fields.String(required=False, validate=fields.Length(min=1, max=120))
    city = fields.String(required=False, validate=fields.Length(min=1, max=120))
    country = fields.String(required=False, validate=fields.Length(min=1, max=120))
    phone = fields.String(required=False, validate=fields.Length(min=1, max=120))

    @post_load
    def make_data(self, data, **kwargs):
        return UserData(**data)