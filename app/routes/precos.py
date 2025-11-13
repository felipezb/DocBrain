from flask import Blueprint, render_template

precos_bp = Blueprint('precos', __name__)

@precos_bp.route('/precos')
def mostrar_precos():
    return render_template('precos.html')