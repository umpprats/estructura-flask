import os
import unittest
from flask import current_app
from app import create_app
from app.mapping.response_schema import ResponseSchema
from app.services.response_message import ResponseBuilder

class HomeResourceTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_index(self):
        message = ResponseBuilder().add_message("Bienvenidos").add_status_code(200).add_data({'title': 'API Auth'}).build()
        client = self.app.test_client(use_cookies=True)
        responseSchema = ResponseSchema()
        #TODO: La URL de la API debe cambiarse por una variable de entorno
        response = client.get('http://localhost:5000/api/v1/')
        self.assertEqual(response.status_code, 200)
        
        response = responseSchema.load(response.get_json())
        self.assertEqual(message.message, response['message'])
        self.assertEqual(message.status_code, response['status_code'])
        self.assertEqual(message.data, response['data'])
        
        

if __name__ == '__main__':
    unittest.main()