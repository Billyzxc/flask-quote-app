from flask import Blueprint,request,jsonify
from app.services.quote_service import create_quote
quote_bp=Blueprint('quotes',__name__)
@quote_bp.route('/',methods=['POST'])
def create():
 q=create_quote(request.json)
 return jsonify(id=q.id),201
