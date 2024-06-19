from marshmallow import validate, fields, Schema


class ResponseSchema(Schema):
    message = fields.String(required=True, validate=validate.Length(min=1))
    status_code = fields.Integer(required=True)
    data = fields.Dict(required=False)
    