from typing import List
from app.models import User
from app.repositories import UserRepository
from app.services import SecurityManager, WerkzeugSecurity
from app import cache

repository = UserRepository()

class UserService:

    """ Clase que se encarga de CRUD de usuarios """
    def __init__(self) -> None:
        self.__security = SecurityManager(WerkzeugSecurity())

    def save(self, user: User) -> User:
        #TODO: Implementar auditoria
        user.password = self.__security.generate_password(user.password)
        return repository.save(user)
    
    def update(self, user: User, id: int) -> User:
        #TODO: Implementar auditoria
        if user.password is not None:
            user.password = self.__security.generate_password(user.password)
            
        return repository.update(user, id)
    
    def delete(self, id: int) -> None:
        #TODO: Implementar auditoria
        user = repository.find(id)
        cache.delete(f'user_{user.id}')
        repository.delete(user)
    
    def all(self) -> List[User]:
        result = cache.get('users')
        if result is None:
            result = repository.all()
            cache.set('users', result, timeout=15)
        return result
    
    def find(self, id: int) -> User:
        result = cache.get(f'user_{id}')
        if result is None:
            result = repository.find(id)
            cache.set(f'user_{id}', result, timeout=15)
        return result
    
    def find_by_username(self, username: str):
        result = cache.get(f'user_{username}')
        if result is None:
            result = repository.find_by_username(username)
            cache.set(f'user_{username}', result, timeout=15)
        return result
    
    def find_by_email(self, email) -> User:
        return repository.find_by_email(email)

    def check_auth(self, username, password) -> bool:
        user = self.find_by_username(username)
        if user is not None:
            return self.__security.check_password(user.password, password)
        else:
            return False