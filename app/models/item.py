from app import db
class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    code=db.Column(db.String(2),unique=True)

class Package(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    code=db.Column(db.String(2))

class Color(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    code=db.Column(db.String(4))

class Item(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    code=db.Column(db.String(20),unique=True)
    category_id=db.Column(db.Integer,db.ForeignKey('category.id'))
    package_id=db.Column(db.Integer,db.ForeignKey('package.id'))
    color_id=db.Column(db.Integer,db.ForeignKey('color.id'))
    serial=db.Column(db.Integer)
