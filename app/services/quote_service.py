from app import db
from app.models.quote import Quote

def create_quote(data):
 q=Quote(**data)
 db.session.add(q)
 db.session.commit()
 return q
