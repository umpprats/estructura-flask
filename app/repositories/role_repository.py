from typing import List
from app.models import Role
from app import db

class RoleRepository:
    """
    RoleRepository class
    """

    def save(self, role: Role) -> Role:
        """
        Save a role
        :param role: Role
        :return: Role
        """
        db.session.add(role)
        db.session.commit()
        return role

    def update(self, role: Role, id: int) -> Role:
        """
        Update a role
        :param role: Role
        :param id: int
        :return: Role
        """
        entity = self.find(id)
        entity.name = role.name
        entity.description = role.description
        db.session.add(entity)
        db.session.commit()
        return role

    def delete(self, role: Role) -> None:
        """
        Delete a role
        :param role: Role
        """
        db.session.delete(role)
        db.session.commit()

    def all(self) -> List[Role]:
        """
        Get all roles
        :return: List[Role]
        """
        return db.session.query(Role).all()

    def find(self, id: int) -> Role:
        """
        Get a role by id
        :param id: int
        :return: Role
        """
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Role).filter(Role.id == id).one()
        except:
            return None

    def find_by_name(self, name: str) -> Role:
        """
        Get a role by name
        :param name: str
        :return: Role
        """
        return db.session.query(Role).filter(Role.name == name).one_or_none()