from flask import Blueprint
from controllers.user_controller import  user_info

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/me', methods=['GET'])
def me():
    return user_info()
