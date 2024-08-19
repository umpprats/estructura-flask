"""
Archivo que se encarga de la autenticación de los usuarios
"""

from functools import wraps
import logging

from flask import jsonify
from flask_jwt_extended import current_user
from app import jwt
from app.services import UserService


@jwt.user_identity_loader
def user_identity_lookup(user):
    """
    Función que se encarga de convertir cualquier objeto Usuario para crear un JWT a un formato serializable JSON.
    """
    logging.info(f"Identity Lookup {user}")
    return user['id']

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    """
    Función que se encarga de buscar un usuario por su id.
    """
    identity = jwt_data["sub"]
    logging.info(f"Lookup Callback {identity}")
    service = UserService()
    return service.find(identity)

@jwt.additional_claims_loader
def add_claims_to_access_token(identity):
    service = UserService()
    logging.info(f"Claims Loader {identity}")
    user = service.find(identity['id'])
    list_roles = [role.name for role in user.roles]
    return {"roles": list_roles}

def roles_required(roles: list[str]):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            logging.info(f"Info {current_user.roles}")
            is_allowed = False
            is_allowed = any(filter(lambda r: r in (role.name for role in current_user.roles), roles)) 
            
            if not is_allowed:
                return jsonify(error='Access denied'), 403
            return fn(*args, **kwargs)

        return decorator

    return wrapper