import os
import unittest
from flask import current_app
from app import create_app
from app import create_app, db

class UserResourceTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_users(self):
        client = self.app.test_client(use_cookies=True)
        response = client.get('http://localhost:5000/api/v1/users')
        self.assertEqual(response.status_code, 200)