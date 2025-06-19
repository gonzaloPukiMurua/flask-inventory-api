from flask import Blueprint, request, jsonify
from app.controllers.product_controller import (
    get_all_products, create_product
)

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    return get_all_products()

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    return create_product(data)

