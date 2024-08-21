from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.auth.authority import roles_required
from app.mapping import UserSchema, ResponseSchema 
from app.services import UserService, ResponseBuilder
from app.validators import validate_with

user = Blueprint('user', __name__)
user_schema = UserSchema()
response_schema = ResponseSchema()
user_service = UserService()

@user.route('/users', methods=['GET'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
def index():
    return {"users": user_schema.dump(user_service.all(),many=True)}, 200

@user.route('/users/<int:id>', methods=['GET'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
def find(id:int):
    """
    id: int ingresado por el usuario
    return: json con los datos del usuario
    """
    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(user_schema.dump(user_service.find(id)))
    return response_schema.dump(response_builder.build()), 200

@user.route('/users/add', methods=['POST'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
@validate_with(UserSchema)
def post_user():
    user = user_schema.load(request.json)
    return {"user": user_schema.dump(user_service.save(user))}, 201


@user.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
@validate_with(UserSchema)
def update_user(id:int):
    user = user_schema.load(request.json)
    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario actualizado").add_status_code(100).add_data( user_schema.dump(user_service.update(user, id)))
    return response_schema.dump(response_builder.build()), 200

@user.route('/users/username/<username>', methods=['GET'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
def find_by_username(username:str):
    response_builder = ResponseBuilder()
    user = user_service.find_by_username(username)
    if user is not None:
        response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(user_schema.dump(user))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Usuario no encontrado").add_status_code(300).add_data({'username': username})
        return response_schema.dump(response_builder.build()), 404

@user.route('/users/email/<email>', methods=['GET'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
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


@user.route('/users/<int:id>', methods=['DELETE'])
@jwt_required()
@roles_required(['ROLE_ADMIN'])
def delete_user(id):
    user_service.delete(id)

    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario borrado").add_status_code(100).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200