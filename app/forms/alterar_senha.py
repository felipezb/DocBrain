from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class AlterarSenhaForm(FlaskForm):
    senha_atual = PasswordField('Senha atual', validators=[DataRequired()])
    nova_senha = PasswordField('Nova senha', validators=[
        DataRequired(),
        Length(min=6, message="A nova senha deve ter pelo menos 6 caracteres.")
    ])
    confirmar_senha = PasswordField('Confirmar nova senha', validators=[
        DataRequired(),
        EqualTo('nova_senha', message='As senhas não coincidem.')
    ])
    submit = SubmitField('Alterar senha')
