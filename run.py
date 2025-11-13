from app import create_app
import traceback
import sys

def main():
    try:
        app = create_app()
    except Exception:
        print("Erro ao criar a aplicação:")
        traceback.print_exc()
        sys.exit(1)

    if __name__ == '__main__':
        try:
            app.run(debug=True)
        except SystemExit as e:
            print(f"SystemExit: {e}")
            raise
        except Exception:
            print("Erro durante app.run():")
            traceback.print_exc()
            raise

if __name__ == "__main__":
    main()