def register_blueprints(app):
    from .item_routes import item_bp
    from .order_routes import order_bp
    from .quote_routes import quote_bp
    from .main_routes import bp as main_bp  # ✅ 加上這行！

    app.register_blueprint(item_bp, url_prefix='/items')
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(quote_bp, url_prefix='/quotes')
    app.register_blueprint(main_bp)  # ✅ 正常註冊首頁路由

