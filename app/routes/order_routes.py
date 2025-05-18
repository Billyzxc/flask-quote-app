from flask import Blueprint,request,jsonify
from app.services.order_code_service import generate_order_code
order_bp=Blueprint('orders',__name__)
@order_bp.route('/',methods=['POST'])
def create():
 d=request.json
 return jsonify(code=generate_order_code(d['category'],d['year'],d['serial'],d['factory']))
