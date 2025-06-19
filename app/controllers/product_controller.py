from app.models.product import Product
from app.extensions import db
from app.schemas.product_schema import product_schema, products_schema

def get_all_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

def create_product(data):
    product = Product(**data)
    db.session.add(product)
    db.session.commmit()
    return product_schema.jsonify(product), 201

