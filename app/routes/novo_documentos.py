from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, Documento

novo_documento_bp = Blueprint('novo_documento', __name__)

@novo_documento_bp.route('/documentos/novo', methods=['GET', 'POST'])
@login_required
def novo_documento():
    if request.method == 'POST':
        cliente = request.form.get('cliente')
        empresa = request.form.get('empresa')
        tipo = request.form.get('tipo')
        valor = request.form.get('valor')
        prazo = request.form.get('prazo')
        observacoes = request.form.get('observacoes')
        conteudo = request.form.get('conteudo')

        if not cliente or not empresa or not tipo or not conteudo:
            flash('Preencha todos os campos obrigatórios.', 'danger')
            return redirect(url_for('novo_documento.novo_documento'))

        documento = Documento(
            titulo=f"{tipo} - {cliente}",
            cliente=cliente,
            empresa=empresa,
            tipo=tipo,
            valor=valor,
            prazo=prazo,
            observacoes=observacoes,
            conteudo=conteudo,
            usuario_id=current_user.id
        )

        db.session.add(documento)
        db.session.commit()
        flash('Documento criado com sucesso!', 'success')
        return redirect(url_for('documentos.historico_documentos'))

    return render_template('novo_documento.html')