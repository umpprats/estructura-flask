from dataclasses import dataclass
from app.models.relations import users_roles
from app import db

@dataclass(init=False, repr=True, eq=True)
class Role (db.Model):
    __tablename__ = 'roles'
    id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), unique=True, nullable=False)
    description: str  = db.Column(db.String(255), nullable=False)
    #Relacion Muchos a Muchos bidireccional con User
    #Flask Web Development Capitulo: Database Relationships Revisited Pag 49,149 
    users = db.relationship("User", secondary=users_roles, back_populates='roles')
    
    #TODO: Implementar metodos para agregar, eliminar y listar usuarios
    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
    
    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
    