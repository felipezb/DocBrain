from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import db, Usuario
from app.forms.alterar_senha import AlterarSenhaForm

configuracoes_bp = Blueprint('configuracoes', __name__)

@configuracoes_bp.route('/configuracoes', methods=['GET', 'POST'])
@login_required
def configuracoes():
    form = AlterarSenhaForm()
    return render_template('configuracoes.html', form=form, usuario=current_user)

@configuracoes_bp.route('/alterar_senha', methods=['POST'])
@login_required
def alterar_senha():
    form = AlterarSenhaForm()
    if form.validate_on_submit():
        if not check_password_hash(current_user.senha, form.senha_atual.data):
            flash('Senha atual incorreta.', 'danger')
            return redirect(url_for('configuracoes.configuracoes'))

        if form.nova_senha.data != form.confirmar_senha.data:
            flash('As senhas não coincidem.', 'danger')
            return redirect(url_for('configuracoes.configuracoes'))

        if len(form.nova_senha.data) < 6:
            flash('A nova senha deve ter pelo menos 6 caracteres.', 'danger')
            return redirect(url_for('configuracoes.configuracoes'))

        current_user.senha = generate_password_hash(form.nova_senha.data)
        db.session.commit()
        flash('Senha alterada com sucesso!', 'success')
    else:
        flash('Preencha todos os campos corretamente.', 'danger')

    return redirect(url_for('configuracoes.configuracoes'))