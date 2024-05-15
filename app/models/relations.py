from app import db
"""
Relacion Muchos a Muchos bidireccional entre User y Role
Se crea una tabla intermedia llamada users_roles
"""
users_roles = db.Table('users_roles',db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True))