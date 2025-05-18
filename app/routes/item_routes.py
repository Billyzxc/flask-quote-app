from flask import Blueprint,request,jsonify
from app.services.item_code_service import generate_item_code
item_bp=Blueprint('items',__name__)
@item_bp.route('/',methods=['POST'])
def create():
 d=request.json
 return jsonify(code=generate_item_code(d['category'],d['package'],d['serial'],d['color']))
