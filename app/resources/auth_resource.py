import logging
from flask import Blueprint, jsonify, request
from flask_apispec import doc, marshal_with, use_kwargs
from app import docs
from flask_jwt_extended import create_access_token

from app.mapping import ResponseSchema, UserSchema 
from app.mapping.login_schema import LoginSchema
from app.services import UserService, ResponseBuilder

auth_bp = Blueprint('auth', __name__)
login_schema = LoginSchema()

@auth_bp.route("/login", methods=["POST"])
@doc(description="Login de Usuario", tags=["Auth"])
@use_kwargs(LoginSchema)
@marshal_with(LoginSchema)
def login(**kwargs):
    user_login = login_schema.load(request.json)
    username = user_login.get("username")
    password = user_login.get("password")
    logging.info(f"Login: {user_login}")
    user_schema = UserSchema()
    service = UserService()
    response_builder = ResponseBuilder()
    response_schema = ResponseSchema()

    if service.check_auth(username, password):
        user = service.find_by_username(username)
        list_roles = [role.name for role in user.roles]
        logging.info(f"User {user.username} with Roles: {list_roles}")
        access_token = create_access_token(user_schema.dump(user), additional_claims={"roles": list_roles})
        return jsonify({"token":access_token, "id": user.id})
    
    response_builder.add_message("Usuario No Autorizado").add_status_code(300).add_data({"message": "Error en Usuario y/o Password"})
    return response_schema.dump(response_builder.build()), 401

@auth_bp.route("/register", methods=["POST"])
@doc(description="Registro de Usuario", tags=["Auth"])
@marshal_with(UserSchema)
def register():
    user_schema = UserSchema()
    service = UserService()
    response_builder = ResponseBuilder()
    response_schema = ResponseSchema()
    user = user_schema.load(request.json)

    if service.save(user):
        response_builder.add_message("Usuario Creado Correctamente").add_status_code(200).add_data(user_schema.dump(user))
        return response_schema.dump(response_builder.build()), 200

    response_builder.add_message("Error al Crear Usuario").add_status_code(300).add_data(user_schema.dump(user))
    return response_schema.dump(response_builder.build()), 400
    