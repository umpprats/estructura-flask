import logging
from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_marshmallow import Marshmallow
from flask_caching import Cache
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.route import RouteApp
from app.config import config
from app.config.cache_config import cache_config
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
jwt = JWTManager()
docs = FlaskApiSpec()
cache = Cache()

def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app_context = os.getenv('FLASK_CONTEXT')
    #https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    docs.init_app(app)
    route = RouteApp()
    route.init_app(app, docs)
    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cache.init_app(app, config=cache_config)
    
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
