from flask import jsonify, request
from webargs.flaskparser import use_args

from app.db.prize_database import PrizeDatabase
from app.schemas.catalog import GetPrizesSchema
from app.validators.catalog_validators import validate_data

from . import catalog_bp

prize_db = PrizeDatabase()

@catalog_bp.route('/<int:catalog_id>/prizes', methods=['GET'])
@validate_data(GetPrizesSchema())
def get_prizes(*args, catalog_id):
    data = request.get_json() if request.get_json() else {}
    result = prize_db.get_prizes(catalog_id, data.get('filter', {}), data.get('pagination', {}))

    return jsonify(result)