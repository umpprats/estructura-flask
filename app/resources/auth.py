import logging
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

from app.mapping.response_schema import ResponseSchema
from app.mapping.user_schema import UserSchema
from app.services import UserService
from app.services.response_message import ResponseBuilder

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
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

@auth.route("/register", methods=["POST"])
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
    