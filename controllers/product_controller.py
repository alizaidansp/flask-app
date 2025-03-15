from models.product import Product
from flask import jsonify
from flask_jwt_extended import jwt_required
from flask import request, jsonify


@jwt_required()  # Protect this route

def get_all_products():
    search_query = request.args.get('search', '').strip()

    # If search_query is provided, filter by name or description
    if search_query:
        products = Product.query.filter(
            (Product.name.ilike(f"%{search_query}%")) |
            (Product.description.ilike(f"%{search_query}%"))
        ).all()
    else:
        products = Product.query.all()

    return jsonify([
        {
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'image': p.image,
            'price': p.price
        } for p in products
    ])