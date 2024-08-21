from flask import jsonify, request
from functools import wraps

from marshmallow import ValidationError

def validate_with(schema):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                data, errors = schema().load(request.json)
            except ValidationError as err:
                return jsonify(err.messages), 400
            return f(*args, **kwargs)
        return decorated_function
    return decorator