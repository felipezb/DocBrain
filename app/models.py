# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db  # usa a instância única definida em app/__init__.py

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    senha = db.Column(db.String(255), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def definir_senha(self, senha_plana):
        self.senha = generate_password_hash(senha_plana)

    def verificar_senha(self, senha_plana):
        return check_password_hash(self.senha, senha_plana)

    def __repr__(self):
        return f"<Usuario {self.email}>"

class Documento(db.Model):
    __tablename__ = 'documentos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    tipo = db.Column(db.String(80))
    cliente = db.Column(db.String(200))
    empresa = db.Column(db.String(200))
    valor = db.Column(db.String(100))
    prazo = db.Column(db.String(100))
    conteudo = db.Column(db.Text)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    usuario = db.relationship('Usuario', backref=db.backref('documentos', lazy=True))

    def __repr__(self):
        return f"<Documento {self.id}>"
