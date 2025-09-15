from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from forms.alterar_senha import AlterarSenhaForm
from app import db

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/alterar_senha', methods=['GET', 'POST'])
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
            return redirect(url_for('main.dashboard'))

    return render_template('alterar_senha.html', form=form)
