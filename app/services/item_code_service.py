from app.models.item import Category, Package, Color
def generate_item_code(cat, pkg, serial, color):
    serial=str(serial).zfill(2)
    c=Category.query.filter_by(name=cat).first().code
    p=Package.query.filter_by(name=pkg).first().code
    col=Color.query.filter_by(name=color).first().code
    return f"{c}{p}{serial}{col}"
