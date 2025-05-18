from flask import Blueprint, request, jsonify
from app.services.quote_service import create_quote
from app.models.quote import Quote  # ✅ 補上這行

quote_bp = Blueprint('quote', __name__)

@quote_bp.route('/', methods=['POST'])
def create():
    q = create_quote(request.json)
    return jsonify(id=q.id), 201

@quote_bp.route('/quotes', methods=['GET'])
def get_all_quotes():
    quotes = Quote.query.order_by(Quote.created_at.desc()).all()
    return jsonify([q.to_dict() for q in quotes])

