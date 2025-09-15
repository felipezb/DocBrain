from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Documento
from utils.ia import gerar_documento_ia

documentos_bp = Blueprint('documentos', __name__)

@documentos_bp.route('/documentos/novo', methods=['GET', 'POST'])
@login_required
def novo_documento():
    if request.method == 'POST':
        doc = Documento(
            tipo=request.form['tipo'],
            cliente=request.form['cliente'],
            empresa=request.form['empresa'],
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

@documentos_bp.route('/documentos/gerar', methods=['POST'])
@login_required
def gerar_documento():
    tipo = request.form['tipo']
    cliente = request.form['cliente']
    empresa = request.form['empresa']
    valor = request.form['valor']
    prazo = request.form['prazo']
    observacoes = request.form['observacoes']

    conteudo_gerado = gerar_documento_ia(tipo, cliente, empresa, valor, prazo, observacoes)

    return render_template('novo_documento.html', conteudo=conteudo_gerado,
                           tipo=tipo, cliente=cliente, empresa=empresa,
                           valor=valor, prazo=prazo, observacoes=observacoes)
    
@documentos_bp.route('/documentos/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_documento(id):
    doc = Documento.query.get_or_404(id)

    if request.method == 'POST':
        doc.conteudo = request.form['conteudo']
        db.session.commit()
        flash('Documento atualizado com sucesso!')
        return redirect(url_for('documentos.editar_documento', id=doc.id))

    return render_template('editar_documento.html', documento=doc)

