# DocBrain – Sistema de Gestão de Documentos com IA

## Descrição

DocBrain é uma aplicação web que utiliza inteligência artificial para organizar, gerar, classificar e buscar documentos de forma eficiente. Desenvolvido com Flask no backend e HTML/CSS/Bootstrap no frontend, o projeto visa facilitar o gerenciamento de arquivos em ambientes corporativos e acadêmicos.

---

## Estrutura do Projeto

```
docbrain/
├── app/
│   ├── static/
│   ├── templates/
│   ├── routes/
│   │   ├── main.py
│   │   ├── auth.py
│   │   ├── documentos.py
│   │   ├── usuarios.py
│   │   └── configuracoes.py
│   ├── models.py
│   ├── forms/
│   │   └── alterar_senha.py
│   ├── utils/
│   │   └── ia.py
│   └── __init__.py
├── instance/
│   └── config.py
├── migrations/
├── requirements.txt
├── config.py
├── run.py
└── README.md
```

---

## Instalação e Execução

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/docbrain.git
   cd docbrain
   ```

2. **Crie e ative o ambiente virtual:**
   - **Windows:**
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure variáveis sensíveis:**
   - Crie o arquivo `instance/config.py` com:
     ```python
     SECRET_KEY = 'sua-chave-secreta'
     SQLALCHEMY_DATABASE_URI = 'sqlite:///docbrain.db'
     ```
   - Ou edite o arquivo `config.py` na raiz do projeto.

   - Para usar a IA, crie um arquivo `.env` na raiz com:
     ```
     OPENAI_API_KEY=sua-chave-openai
     ```

5. **Execute as migrações do banco de dados (opcional):**
   ```sh
   flask db upgrade
   ```

6. **Execute a aplicação:**
   ```sh
   python run.py
   ```
   Acesse em: [http://localhost:5000](http://localhost:5000)

---

## Tecnologias Utilizadas

- Python 3.11+
- Flask
- Flask-Login
- Flask-WTF
- SQLAlchemy
- Bootstrap 5
- HTML5 + CSS3
- OpenAI API (para geração de documentos)
- Git + GitHub
- WeasyPrint 

---

## Funcionalidades

- Autenticação de usuários (login e cadastro)
- Alteração de senha via modal
- Geração de documentos comerciais com IA (OpenAI)
- Upload, classificação e busca inteligente de documentos
- Dashboard com estatísticas e gráficos
- Histórico de documentos
- Exportação de documentos para PDF (em desenvolvimento)
- Interface responsiva e moderna

---

## Como usar

1. Cadastre-se e faça login.
2. Gere novos documentos preenchendo o formulário e usando a IA.
3. Visualize, edite e salve seus documentos.
4. Acesse o dashboard para acompanhar suas estatísticas.
5. Altere sua senha e configure sua conta na área de configurações.

---

## Contribuição

Contribuições são bem-vindas!  
Abra uma issue ou envie um pull request.

---

## Autor

Felipe Zanella Barbosa  
[GitHub](https://github.com/felipezb)  
felipezanella18@gmail.com

---

## Licença

Este projeto está sob a licença MIT.