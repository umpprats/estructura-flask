import unittest
from flask import current_app
from app import create_app
from app.models import Role

class RoleTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_role(self):
        user = Role()
        user.name = 'ROLE_ADMIN'
        user.description = 'Administrator'
        self.assertTrue(user.name, 'ROLE_ADMIN')
        self.assertTrue(user.description, 'Administrator')

if __name__ == '__main__':
    unittest.main()