from flask import Blueprint, jsonify
from app.models.quote import Quote

quote_bp = Blueprint("quote", __name__)

@quote_bp.route("/", methods=["GET"])
def list_quotes():
    quotes = Quote.query.all()
    return jsonify([q.to_dict() for q in quotes])
