from flask import Blueprint

catalog_bp = Blueprint('catalog', __name__)

from . import catalog_routes
