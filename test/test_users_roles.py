import unittest
from flask import current_app
from app import create_app
from app.models import Role, User, UserData
from app import db
from app.services import RoleService, UserService

role_service = RoleService()
user_service = UserService()

class UsersRoleTestCase(unittest.TestCase):
    
        def setUp(self):
            self.app = create_app()
            self.app_context = self.app.app_context()
            self.app_context.push()
            self.ROL_ADMIN = 'ROLE_ADMIN'
            self.ROL_ADMIN_DESC = 'Administrator'
            self.ROL_USER = 'ROLE_USER'
            self.ROL_USER_DESC = 'User'
            self.USERNAME_PRUEBA = 'pabloprats'
            self.EMAIL_PRUEBA = 'test@test.com'
            self.PASSWORD_PRUEBA = '123456'
            self.ADDRESS_PRUEBA = 'Address 1234'
            self.FIRSTNAME_PRUEBA = 'Pablo'
            self.LASTNAME_PRUEBA = 'Prats'
            self.PHONE_PRUEBA = '54260123456789'
            self.CITY_PRUEBA = 'San Rafael'
            self.COUNTRY_PRUEBA = 'Argentina'
            self.app_context.push()
            db.create_all()
    
        def tearDown(self):
            db.session.remove()
            db.drop_all()
            self.app_context.pop()
    
        def test_app(self):
            self.assertIsNotNone(current_app)
        
        def test_role_save(self):
            role = Role(name=self.ROL_ADMIN, description=self.ROL_ADMIN_DESC)
            role.add_user(self.__get_user())
            role_service.save(role)

            self.assertGreaterEqual(role.id, 1)
            self.assertTrue(role.name, self.ROL_ADMIN)
            self.assertTrue(role.description, self.ROL_ADMIN_DESC)
            self.assertGreaterEqual(len(role.users) , 1)
            self.assertTrue(role.users[0].username, self.USERNAME_PRUEBA)
        
        def test_user_save(self):
            user = self.__get_user()
            user.add_role(Role(name=self.ROL_ADMIN, description=self.ROL_ADMIN_DESC))
            user.add_role(Role(name=self.ROL_USER, description=self.ROL_USER_DESC))
            user_service.save(user)
            
            self.assertGreaterEqual(user.id, 1)
            self.assertTrue(user.email, self.EMAIL_PRUEBA)
            self.assertTrue(user.username, self.USERNAME_PRUEBA)
            self.assertIsNotNone(user.password)
            self.assertIsNotNone(user.data)
            self.assertTrue(user.data.address, self.ADDRESS_PRUEBA)
            self.assertTrue(user.data.firstname, self.FIRSTNAME_PRUEBA)
            self.assertTrue(user.data.lastname, self.LASTNAME_PRUEBA)
            self.assertTrue(user.data.phone, self.PHONE_PRUEBA)
            self.assertGreaterEqual(len(user.roles) , 1)
            self.assertTrue(user.roles[0].name, self.ROL_ADMIN)
            self.assertTrue(user.roles[1].name, self.ROL_USER)
    
        def __get_user(self):
            data = UserData()
            data.firstname = self.FIRSTNAME_PRUEBA
            data.lastname = self.LASTNAME_PRUEBA
            data.phone = self.PHONE_PRUEBA
            data.address = self.ADDRESS_PRUEBA
            data.city = self.CITY_PRUEBA
            data.country = self.COUNTRY_PRUEBA
            
            user = User(data)
            user.username = self.USERNAME_PRUEBA
            user.email = self.EMAIL_PRUEBA
            user.password = self.PASSWORD_PRUEBA

            return user