from flask import Flask
from .models import db
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='quote_secret'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///quotes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(main)
    return app
