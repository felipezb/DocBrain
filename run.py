# run.py

from app import create_app
import traceback
import sys

def main():
    try:
        app = create_app()
    except Exception:
        print("\n Erro ao criar a aplicação:")
        traceback.print_exc()
        sys.exit(1)

    try:
        print("\n Iniciando DocBrain em http://localhost:5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
    except SystemExit as e:
        print(f"\n Encerrado com SystemExit: {e}")
        raise
    except Exception:
        print("\n Erro durante execução do app:")
        traceback.print_exc()
        raise

if __name__ == "__main__":
    main()