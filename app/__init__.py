from flask import Flask
from flask_marshmallow import Marshmallow
import os

ma = Marshmallow()

def create_app() -> None:
    config_name = os.getenv('FLASK_ENV')
    app = Flask(__name__)
    ma.init_app(app)

    from app.resources import home
    app.register_blueprint(home, url_prefix='/api/v1')
    
  
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
