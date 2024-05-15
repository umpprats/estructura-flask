from typing import List
from app.models import Role
from app.repositories import RoleRepository

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
        return role

    def update(self, role: Role, id: int) -> Role:
        """
        Update a role
        :param role: Role
        :param id: int
        :return: Role
        """
        repository.update(role, id)
        return role

    def delete(self, role: Role) -> None:
        """
        Delete a role
        :param role: Role
        """
        repository.delete(role)

    def all(self) -> List[Role]:
        """
        Get all roles
        :return: List[Role]
        """
        return repository.all()

    def find(self, id: int) -> Role:
        """
        Get a role by id
        :param role_id: int
        :return: Role
        """
        return repository.find(id)

    def find_by_name(self, name: str) -> Role:
        """
        Get a role by name
        :param name: str
        :return: Role
        """
        return repository.find_by_name(name=name)

    