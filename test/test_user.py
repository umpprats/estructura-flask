import unittest
from flask import current_app
from app import create_app
from app.models import User, UserData
from app import create_app, db

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_user(self):
        
        data = UserData()
        data.surname = 'surname'
        data.address = 'address 1234'
        data.city = 'city'
        data.country = 'country'
        data.phone = '542605502105'
    
        user = User(data)
        user.email = 'test@test.com'
        user.username = 'test'
        user.password = 'test1234'

        self.assertTrue(user.email, 'test@test.com')
        self.assertTrue(user.username, 'test')
        self.assertTrue(user.password, 'test1234')
        self.assertIsNotNone(user.data)
        self.assertTrue(user.data.surname, 'surname')
        self.assertTrue(user.data.address, 'address 1234')
        self.assertTrue(user.data.phone, '542605502105')   


if __name__ == '__main__':
    unittest.main()
