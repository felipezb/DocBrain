from flask import Blueprint, render_template, redirect, url_for
from flask_login import flash, login_required, logout_user

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/precos')
def precos():
    return render_template('precos.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sessão encerrada.')
    return redirect(url_for('auth.login'))