from app import create_app, db
from app.models import Usuario, Documento

app = create_app()

with app.app_context():
    print("Criando banco de dados...")
    db.create_all()
    print("✓ Banco de dados criado com sucesso!")
    print("✓ Arquivo: docbrain.db")
    
    # Listar tabelas
    from sqlalchemy import inspect
    inspector = inspect(db.engine)
    tabelas = inspector.get_table_names()
    print(f"✓ Tabelas: {tabelas}")