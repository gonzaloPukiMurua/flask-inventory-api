from .product_routes import product_bp

def register_blueprints(app):
    app.register_blueprint(product_bp, url_prefix="/api")