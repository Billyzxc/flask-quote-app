from app.models.item import Category
from app.models.order import Factory
def year_code(year):
    return chr(ord('A')+(year-2024)%26)
def generate_order_code(cat,year,serial,factory):
    serial=str(serial).zfill(2)
    c=Category.query.filter_by(name=cat).first().code
    y=year_code(year)
    f=Factory.query.filter_by(name=factory).first().code
    return f"{c}{y}{serial}{f}"
