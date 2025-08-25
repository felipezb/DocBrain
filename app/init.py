from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .routes.main import main_bp
from .routes.auth import auth_bp
from .models import Usuario

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    login_manager.init_app(app)


    from .routes.main import main_bp

    # Registrar blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app

