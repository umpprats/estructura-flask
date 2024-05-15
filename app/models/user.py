from dataclasses import dataclass
from typing import List
from .user_data import UserData
from app import db
from app.models.relations import users_roles

@dataclass(init=False, repr=True, eq=True)
class User(db.Model):
    __tablename__ = 'users'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    password: str = db.Column('password', db.String(255), nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    #Relacion Uno a Uno bidireccional con UserData
    data = db.relationship('UserData', uselist=False, back_populates='user') # type: ignore
    #Relacion Muchos a Muchos bidireccional con Role
    #Flask Web Development Capitulo: Database Relationships Revisited Pag 49,149 
    roles = db.relationship("Role", secondary=users_roles, back_populates='users')
    
    def __init__(self, user_data: UserData = None):
        self.data = user_data
    
    #TODO: Implementar metodos para agregar, eliminar y listar roles