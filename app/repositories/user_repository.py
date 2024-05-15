from typing import List, Type
from app.models import User
from app import db

class UserRepository:
    """
    Aplicamos Responsabilidad Única y el Patrón Repository https://martinfowler.com/eaaCatalog/repository.html
    """
    def save(self, user: User) -> User:
        db.session.add(user) 
        db.session.commit()
        return user
    
    def update(self, user: User, id: int) -> User:
        entity = self.find(id)
        entity.username = user.username
        entity.email = user.email
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, user: User) -> None:
        db.session.delete(user)
        db.session.commit()
    
    def all(self) -> List[User]:
        users = db.session.query(User).all()
        return users
    
    def find(self, id: int) -> User:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(User).filter(User.id == id).one()
        except:
            return None
        
    def find_by_username(self, username: str):
        return db.session.query(User).filter(User.username == username).one_or_none()
    
    def find_by_email(self, email: str) -> list[User]:
        #busqueda por like
        return db.session.query(User).filter(User.email.like(f'%{email}%')).all()

    