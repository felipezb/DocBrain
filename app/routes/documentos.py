from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime
from app import db  
from models import Documento  

documentos_bp = Blueprint('documentos', __name__, url_prefix='/documentos')

@documentos_bp.route('/novo', methods=['GET', 'POST'])
@login_required
def novo_documento():
    if request.method == 'POST':
        doc = Documento(
            tipo=request.form['tipo'],
            cliente=request.form['cliente'],
            empresa=request.form['empresa'],
            servico=request.form['servico'],
            valor=request.form['valor'],
            prazo=request.form['prazo'],
            observacoes=request.form['observacoes'],
            usuario_id=current_user.id
        )
        db.session.add(doc)
        db.session.commit()
        flash('Documento salvo com sucesso!')
        return redirect(url_for('main.dashboard'))
    return render_template('novo_documento.html')
