from marshmallow import validate, fields, Schema

class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True)