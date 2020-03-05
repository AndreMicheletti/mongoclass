from app.app import create_flask_app

if __name__ == "__main__":  # pragma: no cover
    flask_app = create_flask_app()
    flask_app.run(debug=True)