import unittest
from flask import current_app
from app import create_app

class HomeResourceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_index(self):
        client = self.app.test_client(use_cookies=True)
        #TODO: La URL de la API debe cambiarse por una variable de entorno
        response = client.get('http://localhost:5000/api/v1/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'OK', response.data)
        

if __name__ == '__main__':
    unittest.main()