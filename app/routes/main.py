from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/precos')
def precos():
    return render_template('precos.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    # Exemplo: dados = Documento.query.filter_by(usuario_id=current_user.id).all()
    return render_template('dashboard.html')