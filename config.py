import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'sua-chave-secreta-dev')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'docbrain.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
