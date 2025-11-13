from flask import Blueprint, render_template, request, redirect, url_for, flash, make_response, render_template_string
from flask_login import login_required, current_user
from app.models import db, Documento
from xhtml2pdf import pisa
from io import BytesIO

documentos_bp = Blueprint('documentos', __name__)

@documentos_bp.route('/documentos/novo', methods=['GET', 'POST'])
@login_required
def novo_documento():
    if request.method == 'POST':
        doc = Documento(
            titulo=f"{request.form['tipo']} - {request.form['cliente']}",
            cliente=request.form['cliente'],
            empresa=request.form['empresa'],
            tipo=request.form['tipo'],
            valor=request.form['valor'],
            prazo=request.form['prazo'],
            observacoes=request.form['observacoes'],
            conteudo=request.form['conteudo'],
            usuario_id=current_user.id
        )
        db.session.add(doc)
        db.session.commit()
        flash('Documento criado com sucesso!', 'success')
        return redirect(url_for('documentos.historico_documentos'))

    return render_template('novo_documento.html')

@documentos_bp.route('/documentos/historico')
@login_required
def historico_documentos():
    documentos = Documento.query.filter_by(usuario_id=current_user.id).order_by(Documento.criado_em.desc()).all()
    return render_template('historico.html', documentos=documentos)

@documentos_bp.route('/documentos/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_documento(id):
    doc = Documento.query.get_or_404(id)
    if doc.usuario_id != current_user.id:
        flash('Você não tem permissão para editar este documento.', 'danger')
        return redirect(url_for('documentos.historico_documentos'))

    if request.method == 'POST':
        doc.conteudo = request.form['conteudo']
        db.session.commit()
        flash('Documento atualizado com sucesso!', 'success')
        return redirect(url_for('documentos.editar_documento', id=doc.id))

    return render_template('editar_documento.html', documento=doc)

@documentos_bp.route('/documentos/<int:id>/exportar_pdf')
@login_required
def exportar_pdf(id):
    doc = Documento.query.get_or_404(id)
    if doc.usuario_id != current_user.id:
        flash('Você não tem permissão para exportar este documento.', 'danger')
        return redirect(url_for('documentos.historico_documentos'))

    html = render_template_string("""
    <html>
    <head>
      <meta charset="UTF-8">
      <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        h1 { color: #0d6efd; }
        p { margin-bottom: 10px; }
      </style>
    </head>
    <body>
      <h1>{{ doc.tipo }}</h1>
      <p><strong>Cliente:</strong> {{ doc.cliente }}</p>
      <p><strong>Empresa:</strong> {{ doc.empresa }}</p>
      <p><strong>Valor:</strong> {{ doc.valor }}</p>
      <p><strong>Prazo:</strong> {{ doc.prazo }}</p>
      <p><strong>Personalização:</strong> {{ doc.observacoes }}</p>
      <hr>
      <p>{{ doc.conteudo }}</p>
    </body>
    </html>
    """, doc=doc)

    pdf = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf)
    if pisa_status.err:
        flash('Erro ao gerar PDF.', 'danger')
        return redirect(url_for('documentos.editar_documento', id=id))

    response = make_response(pdf.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=documento_{id}.pdf'
    return response