import unittest
from flask import current_app
from app import create_app
from app.models import Role

class RoleTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.ROL_NAME = 'ROLE_ADMIN'
        self.ROL_DESCRIPCION = 'Administrator'

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_role(self):
        role = self.__get_role()
        self.assertTrue(role.name, 'ROLE_ADMIN')
        self.assertTrue(role.description, 'Administrator')
    
    def __get_role(self) -> Role:
        role = Role()
        role.name = self.ROL_NAME
        role.description = self.ROL_DESCRIPCION
        return role

if __name__ == '__main__':
    unittest.main()