from flask import Blueprint, request, jsonify
from app.services.quote_service import create_quote

quote_bp = Blueprint('quote', __name__)  # 注意名稱用 quote，不是 quotes

@quote_bp.route('/', methods=['POST'])
def create():
    q = create_quote(request.json)
    return jsonify(id=q.id), 201

@quote_bp.route('/quotes', methods=['GET'])
def get_all_quotes():
    return jsonify({"message": "Quote list will be returned here."})

