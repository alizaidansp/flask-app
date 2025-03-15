from flask import jsonify, g
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()  # Protect this route
def user_info():
    user = User.query.first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'status': user.status
    }), 200
