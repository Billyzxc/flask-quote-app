from app import db

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_number = db.Column(db.String(50))
    product_desc = db.Column(db.Text)
    overall_dim = db.Column(db.String(50))
    material = db.Column(db.String(120))
    finish = db.Column(db.String(120))
    loading = db.Column(db.Float)
    price = db.Column(db.Numeric(10, 2))
    color = db.Column(db.String(50))
    fob_location = db.Column(db.String(60))
    package_type = db.Column(db.String(60))
    set_per_carton = db.Column(db.Integer)
    carton_size = db.Column(db.String(50))
    cuft = db.Column(db.Float)
    net_weight = db.Column(db.Float)
    gross_weight = db.Column(db.Float)
    max_load_40gp = db.Column(db.Integer)
    moq = db.Column(db.Integer)
    feature_1 = db.Column(db.String(200))
    feature_2 = db.Column(db.String(200))
    feature_3 = db.Column(db.String(200))
    img_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "item_number": self.item_number,
            "product_desc": self.product_desc,
            "overall_dim": self.overall_dim,
            "material": self.material,
            "finish": self.finish,
            "loading": self.loading,
            "price": float(self.price) if self.price else None,
            "color": self.color,
            "fob_location": self.fob_location,
            "package_type": self.package_type,
            "set_per_carton": self.set_per_carton,
            "carton_size": self.carton_size,
            "cuft": self.cuft,
            "net_weight": self.net_weight,
            "gross_weight": self.gross_weight,
            "max_load_40gp": self.max_load_40gp,
            "moq": self.moq,
            "feature_1": self.feature_1,
            "feature_2": self.feature_2,
            "feature_3": self.feature_3,
            "img_url": self.img_url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

