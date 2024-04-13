from dataclasses import dataclass
from .user_data import UserData
from app import db

@dataclass(init=False, repr=True, eq=True)
class User(db.Model):
    __tablename__ = 'users'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    password: str = db.Column(db.String(120), nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False) 
    data = db.relationship('UserData', uselist=False, back_populates='user') # type: ignore

    def __init__(self, user_data: UserData = None):
        self.data = UserData()
