from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class UserData(db.Model):
    __tablename__ = 'users_data'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surname: str = db.Column(db.String(80), nullable=False)
    phone: str = db.Column(db.String(120), nullable=False)
    address: str = db.Column(db.String(120), nullable=False)
    city: str   = db.Column(db.String(120), nullable=False)
    country: str = db.Column(db.String(120), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates='data', uselist=False)