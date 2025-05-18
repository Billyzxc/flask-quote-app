
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote_no = db.Column(db.String(50))
    client_name = db.Column(db.String(100))
    product_name = db.Column(db.String(150))
    unit_price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Float)
    quote_date = db.Column(db.String(20))
    notes = db.Column(db.Text)
