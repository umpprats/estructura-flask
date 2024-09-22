from asyncio.log import logger
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    APISPEC_SPEC = APISpec(
        title='Estructura Flask API', 
        version='1.0.0', 
        openapi_version='2.0', 
        plugins=[MarshmallowPlugin()],
        authorizations={
            'description': 'Authorization HTTP header with JWT access token, like: Authorization: Bearer asdf.qwer.zxcv',
            'in': 'header',
            'type': 'string',
            'required': True
        }
    )
    APISPEC_SECURITY_DEFINITIONS = {
        'bearerAuth': {
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT'
        }
    }

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
        
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_RECORD_QUERIES = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI')
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

def factory(app):
    configuration = {
        'testing': TestConfig,
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }
    
    return configuration[app]