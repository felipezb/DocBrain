from flask import flash, Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from urllib.parse import urlparse
from sqlalchemy.exc import IntegrityError
from app.models import Usuario
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        senha = request.form.get('senha', '').strip()
        remember = bool(request.form.get('remember'))

        if not email or not senha:
            flash('Preencha todos os campos.', 'warning')
            return render_template('login.html')

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.verificar_senha(senha):
            login_user(usuario, remember=remember)
            flash('Login realizado com sucesso!', 'success')
            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('main.dashboard')
            return redirect(next_page)
        flash('Credenciais inválidas.', 'danger')

    return render_template('login.html')


@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    print("[DEBUG] Rota /cadastro acessada")
    if request.method == 'POST':
        print("[DEBUG] POST recebido")
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip().lower()
        senha = request.form.get('senha', '').strip()
        confirmar = request.form.get('confirmar_senha', '').strip()

        if not nome or not email or not senha or not confirmar:
            flash('Preencha todos os campos.', 'warning')
            return redirect(url_for('auth.cadastro'))

        if len(senha) < 6:
            flash('A senha deve ter pelo menos 6 caracteres.', 'warning')
            return redirect(url_for('auth.cadastro'))

        if senha != confirmar:
            flash('As senhas não coincidem.', 'danger')
            return redirect(url_for('auth.cadastro'))

        novo_usuario = Usuario(nome=nome, email=email)
        novo_usuario.definir_senha(senha)

        try:
            db.session.add(novo_usuario)
            db.session.commit()
            print(f"[DEBUG] Usuário {email} criado com sucesso!")
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('auth.login'))
        except IntegrityError as e:
            db.session.rollback()
            print(f"[DEBUG] IntegrityError - Email {email} já existe! Erro: {str(e)}")
            flash('E-mail já cadastrado.', 'danger')
            return redirect(url_for('auth.cadastro'))
        except Exception as e:
            db.session.rollback()
            print(f"[DEBUG] Exceção geral ao criar usuário:")
            print(f"[DEBUG] Tipo: {type(e).__name__}")
            print(f"[DEBUG] Mensagem: {str(e)}")
            import traceback
            traceback.print_exc()
            flash('Erro ao criar usuário. Tente novamente.', 'danger')
            return redirect(url_for('auth.cadastro'))

    return render_template('cadastro.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('main.index'))
