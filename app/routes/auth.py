from flask import flash, Blueprint, render_template, request, redirect, url_for
from flask_login import login_user
from app.models import Usuario
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '').strip()
        if not email or not senha:
            flash('Preencha todos os campos.', 'warning')
            return render_template('login.html')
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.verificar_senha(senha):
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.dashboard'))
        else:
            flash('Credenciais inválidas.', 'danger')
    return render_template('login.html')


@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '').strip()
        confirmar = request.form.get('confirmar_senha', '').strip()

        if not nome or not email or not senha or not confirmar:
            flash('Preencha todos os campos.', 'warning')
            return redirect(url_for('auth.cadastro'))

        if senha != confirmar:
            flash('As senhas não coincidem.', 'danger')
            return redirect(url_for('auth.cadastro'))

        if Usuario.query.filter_by(email=email).first():
            flash('E-mail já cadastrado.', 'danger')
            return redirect(url_for('auth.cadastro'))

        novo_usuario = Usuario(nome=nome, email=email)
        novo_usuario.definir_senha(senha)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('cadastro.html')
