from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models.user import User, db

# Register User
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Validate input
    if not (username and email and password):
        return jsonify({'error': 'Missing required fields'}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'User already exists'}), 409

    # Create new user
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    # print(new_user.id)

    # Generate JWT token
    access_token = create_access_token(identity=new_user.id)

    return jsonify({'message': 'User registered successfully', 'access_token': access_token}), 201

# Login User
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Validate input
    if not (email and password):
        return jsonify({'error': 'Missing email or password'}), 400

    # Find user and check password
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    # Generate JWT token
    access_token = create_access_token(identity=user.id)

    return jsonify({'message': 'Login successful', 'access_token': access_token}), 200
