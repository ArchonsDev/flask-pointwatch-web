from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from os import urandom

from .controllers.auth_controller import auth_bp
from .models import db

def create_app():
    app = Flask(__name__)
    app.secret_key = urandom(32)
    app.config.from_object('config')

    app.register_blueprint(auth_bp, url_prefix='/auth')

    db.init_app(app)

    jwt = JWTManager(app)

    return app

app = create_app()
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
