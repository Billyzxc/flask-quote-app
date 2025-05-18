from app import db
class Factory(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    code=db.Column(db.String(2))

class Order(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    code=db.Column(db.String(20),unique=True)
    serial=db.Column(db.Integer)
