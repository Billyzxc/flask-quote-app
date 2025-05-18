from flask import Blueprint, redirect, url_for

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return redirect(url_for('quote.get_all_quotes'))  # 指向 quote blueprint 中的 /quotes

