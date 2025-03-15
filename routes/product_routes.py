from flask import Blueprint
from controllers.product_controller import get_all_products

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    return get_all_products()