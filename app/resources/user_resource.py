from flask import Blueprint, request
from flask_apispec import doc, marshal_with, use_kwargs
from flask_jwt_extended import jwt_required
from app.auth.authority import roles_required
from app.mapping import UserSchema, ResponseSchema 
from app.services import UserService, ResponseBuilder
from app.validators import validate_with

user_bp = Blueprint('user', __name__)
user_schema = UserSchema()
response_schema = ResponseSchema()
user_service = UserService()

@user_bp.route('/users', methods=['GET'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
@doc(description='Get all Users', tags=['User'], params={ 'Authorization': { 'description': 'Authorization: Bearer asdf.qwer.zxcv', 'in': 'header', 'type': 'string', 'required': True } } )
@marshal_with(UserSchema(many=True))
def index():
    return user_schema.dump(user_service.all(),many=True), 200


@user_bp.route('/users/<int:id>', methods=['GET'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
@doc(description='Get User by Id', tags=['User'], params={ 'Authorization': { 'description': 'Authorization: Bearer asdf.qwer.zxcv', 'in': 'header', 'type': 'string', 'required': True } } )
@marshal_with(ResponseSchema)
def find(id:int):
    """
    id: int ingresado por el usuario
    return: json con los datos del usuario
    """
    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(user_schema.dump(user_service.find(id)))
    return response_schema.dump(response_builder.build()), 200

@user_bp.route('/users/add', methods=['POST'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
@validate_with(UserSchema)
@use_kwargs(UserSchema)
@doc(description='Add User', tags=['User'], params={ 'Authorization': { 'description': 'Authorization: Bearer asdf.qwer.zxcv', 'in': 'header', 'type': 'string', 'required': True } } )
@marshal_with(UserSchema, code=201)
def post_user(**kwargs):
    user = user_schema.load(request.json)
    return user_schema.dump(user_service.save(user)), 201


@user_bp.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
@validate_with(UserSchema)
@use_kwargs(UserSchema)
@doc(description='Update User by Id', tags=['User'], params={ 'Authorization': { 'description': 'Authorization: Bearer asdf.qwer.zxcv', 'in': 'header', 'type': 'string', 'required': True } } )
@marshal_with(ResponseSchema, code=202)
def update_user(id:int, **kwargs):
    user = user_schema.load(request.json)
    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario actualizado").add_status_code(100).add_data( user_schema.dump(user_service.update(user, id)))
    return response_schema.dump(response_builder.build()), 202

@user_bp.route('/users/username/<username>', methods=['GET'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
@doc(description='Get User by username', tags=['User'], params={ 'Authorization': { 'description': 'Authorization: Bearer asdf.qwer.zxcv', 'in': 'header', 'type': 'string', 'required': True } } )
@marshal_with(ResponseSchema, code=200)
def find_by_username(username:str):
    response_builder = ResponseBuilder()
    user = user_service.find_by_username(username)
    if user is not None:
        response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(user_schema.dump(user))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Usuario no encontrado").add_status_code(300).add_data({'username': username})
        return response_schema.dump(response_builder.build()), 404

@user_bp.route('/users/email/<email>', methods=['GET'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
@doc(description='Get User by email', tags=['User'], params={ 'Authorization': { 'description': 'Authorization: Bearer asdf.qwer.zxcv', 'in': 'header', 'type': 'string', 'required': True } } )
@marshal_with(ResponseSchema, code=200)
def find_by_email(email:str):
    response_builder = ResponseBuilder()
    user = user_service.find_by_email(email)
    print(f'{user}')
    if user is not None:
        response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(user_schema.dump(user))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Usuario no encontrado").add_status_code(300).add_data({'email': email})
        return response_schema.dump(response_builder.build()), 404


@user_bp.route('/users/<int:id>', methods=['DELETE'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
@doc(description='Delete by Id', tags=['User'], params={ 'Authorization': { 'description': 'Authorization: Bearer asdf.qwer.zxcv', 'in': 'header', 'type': 'string', 'required': True } } )
@marshal_with(ResponseSchema, code=204)
def delete_user(id):
    user_service.delete(id)

    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario borrado").add_status_code(100).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 204