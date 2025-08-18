from flask import Flask
from .config import Config
from .extensions import db, ma

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    from .resources import api_bp
    app.register_blueprint(api_bp)

    return app

