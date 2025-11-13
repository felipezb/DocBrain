from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from app.models import Usuario

# Instâncias globais das extensões
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializa extensões com a aplicação
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Configurações do Flask-Login
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # Importa e registra os blueprints
    from app.routes.home import home_bp
    from app.routes.precos import precos_bp
    from app.routes.auth import auth_bp
    from app.routes.documentos import documentos_bp
    from app.routes.usuarios import usuarios_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(precos_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(documentos_bp)
    app.register_blueprint(usuarios_bp)
  
    

    return app