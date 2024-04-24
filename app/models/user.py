from dataclasses import dataclass
from typing import List
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
        self.data = user_data

    """
    Aplico el patrón Active Record https://www.martinfowler.com/eaaCatalog/activeRecord.html, donde el modelo se encarga de la persistencia de los datos.
    Este patrón es muy útil para aplicaciones pequeñas y medianas, pero no es recomendable para aplicaciones grandes.
    Puede llegar a contradecir los principios SOLID http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod, ya que el modelo tiene responsabilidades de persistencia y de negocio.
    
    """

    def save(self) -> 'User':
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def all(cls) -> List['User']:
        return cls.query.all()

    @classmethod
    def find(cls, id: int) -> 'User':
        return cls.query.get(id)

    @classmethod
    def find_by(cls, **kwargs) -> List['User']:
        return cls.query.filter_by(**kwargs).all()
