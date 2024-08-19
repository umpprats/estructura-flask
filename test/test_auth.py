import unittest
from flask import current_app
from app.mapping import UserSchema
from app.models import User, UserData
from app import create_app, db
import os
from app.services import UserService

user_service = UserService()
user_schema = UserSchema()

class AuthTestCase(unittest.TestCase):

    def setUp(self):

        self.USERNAME_PRUEBA = 'pabloprats'
        self.EMAIL_PRUEBA = 'test@test.com'
        self.PASSWORD_PRUEBA = '123456'
        self.ADDRESS_PRUEBA = 'Address 1234'
        self.FIRSTNAME_PRUEBA = 'Pablo'
        self.LASTNAME_PRUEBA = 'Prats'
        self.PHONE_PRUEBA = '54260123456789'
        self.CITY_PRUEBA = 'San Rafael'
        self.COUNTRY_PRUEBA = 'Argentina'

        os.environ['FLASK_CONTEXT'] = 'testing'
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
    
    def test_login(self):
        # Verificar que devuelve un bearer token
        user = self.__get_user()
        user_service.save(user)
        client = self.app.test_client(use_cookies=True)
        response = client.post('http://localhost:5000/api/v1/auth/login', json= {
            'username': self.USERNAME_PRUEBA,
            'password': self.PASSWORD_PRUEBA
        })
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json['token'])
        self.assertGreaterEqual(len(response.json['token']), 10)
        self.assertGreaterEqual(response.json['token'].count('.'), 2)

    def __get_user(self):
        
        data = UserData()
        data.firstname = self.FIRSTNAME_PRUEBA
        data.lastname = self.LASTNAME_PRUEBA
        data.phone = self.PHONE_PRUEBA
        data.address = self.ADDRESS_PRUEBA
        data.city = self.CITY_PRUEBA
        data.country = self.COUNTRY_PRUEBA
        
        user = User()
        user.data = data
        user.username = self.USERNAME_PRUEBA
        user.email = self.EMAIL_PRUEBA
        user.password = self.PASSWORD_PRUEBA
        
        return user

if __name__ == '__main__':
    unittest.main()