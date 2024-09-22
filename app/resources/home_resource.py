from flask import jsonify, Blueprint
from flask_apispec import doc
from app.mapping.response_schema import ResponseSchema
from app.services.response_message import ResponseBuilder

home_bp = Blueprint('home', __name__)

response_schema = ResponseSchema()

@doc(description='Home - Bienvenidos', tags=['Home'])
@home_bp.route('/', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    response_builder.add_message("Bienvenidos").add_status_code(200).add_data({'title': 'API Auth'})
    response = response_builder.build()
    return response_schema.dump(response), 200