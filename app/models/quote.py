from app import db
class Quote(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    item_number=db.Column(db.String(50))
    price=db.Column(db.Numeric(10,2))
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())

    def to_dict(self):
        return {"id": self.id, "item_number": self.item_number, "price": float(self.price)}
