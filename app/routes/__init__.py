def register_blueprints(app):
    from .quote_routes import quote_bp
    app.register_blueprint(quote_bp, url_prefix="/quotes")
