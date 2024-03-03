from flask import Flask
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv()

    from app.routes.catalog_routes import catalog_bp
    app.register_blueprint(catalog_bp, url_prefix='/api/catalogs')

    return app
