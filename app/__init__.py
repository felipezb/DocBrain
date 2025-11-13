from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # inicializa extensões
    db.init_app(app)
    login_manager.init_app(app)

    # agora importe modelos / blueprints (evita import antes do init_app)
    from .models import Usuario
    from .routes.main import main_bp
    from .routes.auth import auth_bp
    from .routes.documentos import documentos_bp
    from .routes.usuarios import usuarios_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(documentos_bp)
    app.register_blueprint(usuarios_bp)

    # carregar usuário para flask-login
    @login_manager.user_loader
    def load_user(user_id):
        from .models import Usuario
        return Usuario.query.get(int(user_id))

    return app

