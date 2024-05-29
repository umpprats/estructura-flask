from dataclasses import dataclass
from app import db
from app.models.audit_mixin import AuditMixin
from app.models.soft_delete import SoftDeleteMixin

@dataclass(init=False, repr=True, eq=True)
class UserData(SoftDeleteMixin, AuditMixin, db.Model):
    __tablename__ = 'users_data'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column(db.String(80), nullable=False)
    lastname: str = db.Column(db.String(80), nullable=False)
    phone: str = db.Column(db.String(120), nullable=False)
    address: str = db.Column(db.String(120), nullable=False)
    city: str   = db.Column(db.String(120), nullable=False)
    country: str = db.Column(db.String(120), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    #Relacion Uno a Uno bidireccional con User
    #Flask Web Development Capitulo: Database Relationships Revisited Pag 49,149 
    user = db.relationship("User", back_populates='data', uselist=False)
    
    #Relacion Muchos a Uno bidireccional con Profile
    profile_id = db.Column('profile_id', db.Integer, db.ForeignKey('profiles.id'))
    profile = db.relationship("Profile", back_populates='data')