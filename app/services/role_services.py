from typing import List
from app.models import Role
from app.repositories import RoleRepository
from app import cache

repository = RoleRepository()

class RoleService:
    """
    RoleService class
    """
    def __init__(self):
        pass

    def save(self, role: Role) -> Role:
        """
        Save a role
        :param role: Role
        :return: Role
        """
        repository.save(role)
        cache.set(f'role_{role.id}', role, timeout=15)
        return role

    def update(self, role: Role, id: int) -> Role:
        """
        Update a role
        :param role: Role
        :param id: int
        :return: Role
        """
        repository.update(role, id)
        cache.set(f'role_{role.id}', role, timeout=15)
        return role

    def delete(self, role: Role) -> None:
        """
        Delete a role
        :param role: Role
        """
        cache.delete(f'role_{role.id}')
        repository.delete(role)

    def all(self) -> List[Role]:
        """
        Get all roles
        :return: List[Role]
        """
        result = cache.get('roles')
        if result is None:
            result = repository.all()
            cache.set('roles', result, timeout=15)
        return result

    def find(self, id: int) -> Role:
        """
        Get a role by id
        :param role_id: int
        :return: Role
        """
        result = cache.get(f'role_{id}')
        if result is None:
            result = repository.find(id)
            cache.set(f'role_{id}', result, timeout=15)
        
        return result 

    def find_by_name(self, name: str) -> Role:
        """
        Get a role by name
        :param name: str
        :return: Role
        """
        return repository.find_by_name(name=name)

    