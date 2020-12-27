from flask import Flask
from .config import ProdConfig,TestConfig,DevConfig
from .utils.database import db
from .backend.views import api_bp
from .backend.models import Todo




def create_app():

    app=Flask(__name__)


    app.config.from_object(DevConfig) if app.debug else app.config.from_object(ProdConfig)

    db.init_app(app)
    

    app.register_blueprint(api_bp,url_prefix='/api')

    @app.shell_context_processor
    def make_shell_context():
        return {
            "app":app,
            "db":db,
            "Todo":Todo
        }
    
    return app