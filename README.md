DocBrain – Sistema de Gestão de Documentos com IA
=================================================

Descrição:
----------
DocBrain é uma aplicação web que utiliza inteligência artificial para organizar, classificar e buscar documentos de forma eficiente. Desenvolvido com Flask no backend e HTML/CSS no frontend, o projeto visa facilitar o gerenciamento de arquivos em ambientes corporativos e acadêmicos.

Estrutura do Projeto:
---------------------
docbrain/
├── app/
│   ├── static/
│   ├── templates/
│   ├── routes/
│   ├── models.py
│   ├── forms.py
│   └── __init__.py
├── instance/
│   └── config.py
├── migrations/
├── requirements.txt
├── run.py
└── README.txt

Instalação e Execução:
----------------------
1. Clone o repositório:
   git clone https://github.com/seu-usuario/docbrain.git
   cd docbrain

2. Crie e ative o ambiente virtual:
   python -m venv venv
   source venv/bin/activate  (Linux/macOS)
   venv\Scripts\activate     (Windows)

3. Instale as dependências:
   pip install -r requirements.txt

4. Configure variáveis sensíveis:
   Crie o arquivo instance/config.py com:
   SECRET_KEY = 'sua-chave-secreta'
   SQLALCHEMY_DATABASE_URI = 'sqlite:///docbrain.db'

5. Execute a aplicação:
   python run.py

   Acesse em: http://localhost:5000

Tecnologias Utilizadas:
------------------------
- Python 3.11+
- Flask
- Flask-Login
- Flask-WTF
- SQLAlchemy
- HTML5 + CSS3
- Git + GitHub

Funcionalidades:
----------------
- Tela de login com autenticação
- Cadastro de usuários
- Upload e classificação de documentos
- Busca inteligente por conteúdo
- Dashboard com estatísticas

Autor:
------
Felipe Zanella Barbosa (https://github.com/felipezb) (felipezanella18@gmail.com)
Desenvolvedor Full Stack apaixonado por IA, automação e soluções que simplificam a vida.