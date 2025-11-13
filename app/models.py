from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    documentos = db.relationship('Documento', backref='autor', lazy=True)

    def __repr__(self):
        return f'<Usuario {self.email}>'

class Documento(db.Model):
    __tablename__ = 'documentos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    cliente = db.Column(db.String(100), nullable=False)
    empresa = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.String(50))
    prazo = db.Column(db.String(50))
    observacoes = db.Column(db.String(200))
    conteudo = db.Column(db.Text, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return f'<Documento {self.titulo}>'