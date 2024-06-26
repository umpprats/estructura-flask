from app.models.user import User
from marshmallow import validate, fields, Schema, post_load

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    email = fields.String(required=True, validate=validate.Email())
    password = fields.String(load_only=True)
    data = fields.Nested("UserDataSchema")
    
    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)