from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.forms.alterar_senha import AlterarSenhaForm
from app import db

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/configuracoes', methods=['GET', 'POST'])
@login_required
def configuracoes():
    form = AlterarSenhaForm()
    # Exemplo: dados do usuário para exibir no template
    nome = current_user.nome
    email = current_user.email

    # Se quiser tratar o formulário principal de configurações (nome/email), faça aqui:
    if request.method == 'POST' and 'Salvar' in request.form.values():
        # Exemplo de atualização de nome/email (implemente conforme seu modelo)
        # current_user.nome = request.form.get('nome')
        # current_user.email = request.form.get('email')
        # db.session.commit()
        flash('Configurações salvas com sucesso!', 'success')
        return redirect(url_for('usuarios.configuracoes'))

    return render_template('configuracoes.html', form=form, nome=nome, email=email)

@usuarios_bp.route('/alterar_senha', methods=['POST'])
@login_required
def alterar_senha():
    form = AlterarSenhaForm()
    if form.validate_on_submit():
        if not check_password_hash(current_user.senha, form.senha_atual.data):
            flash('Senha atual incorreta.', 'danger')
        else:
            current_user.senha = generate_password_hash(form.nova_senha.data)
            db.session.commit()
            flash('Senha alterada com sucesso!', 'success')
    else:
        flash('Erro ao alterar senha. Verifique os dados informados.', 'danger')
    return redirect(url_for('usuarios.configuracoes'))