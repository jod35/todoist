from flask import Flask
from .config import ProdConfig,TestConfig,DevConfig
from .utils.database import db
from .backend.views import api_bp
from .frontend.views import ui_bp
from .backend.models import Todo
from flask_migrate import Migrate



def create_app():

    app=Flask(__name__,static_folder='static')


    app.config.from_object(DevConfig) if app.debug else app.config.from_object(ProdConfig)

    db.init_app(app)
    migrate=Migrate(app,db)

    app.register_blueprint(api_bp,url_prefix='/api')
    app.register_blueprint(ui_bp,url_prefix='/')

    @app.shell_context_processor
    def make_shell_context():
        return {
            "app":app,
            "db":db,
            "Todo":Todo
        }
    
    return app