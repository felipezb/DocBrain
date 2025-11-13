# config.py
import os

# Diretório base do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Chave secreta para sessões e CSRF
    SECRET_KEY = os.getenv(
        'SECRET_KEY',
        'cfb2f99a36f08feaf8f7cf5e13492fd966d4754907386bddfd1c28330494ee4e'
    )

    # Banco de dados SQLite (local)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///' + os.path.join(basedir, 'instance', 'docbrain.db')
    )

    # Configurações do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO', 'False').lower() == 'true'

    # Ambiente e debug
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

    # Segurança de cookies e sessões
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_PROTECTION = 'strong'