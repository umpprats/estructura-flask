import os

class Config(object):
    FLASK_ENV = 'production'
    OTEL_PYTHON_LOG_CORRELATION= True
    DEBUG = False
    TESTING = False
    CONNECTION_STRING = os.environ.get('APPLICATIONINSIGHTS_CONNECTION_STRING')
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)