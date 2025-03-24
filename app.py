# app.py
from flask import Flask, jsonify
import os
from extensions import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*":{"origins":"*" }})

    # Dynamically set database path based on environment
    # ec2_db_path = 'sqlite://///home/ali/all-dev/PHASE-2/AWS/3_catalog_project/flask_app/catalog.db' #(local)
   
    # ec2_db_path = 'sqlite:////home/ubuntu/catalog_server/catalog.db' #(prod)

    ec2_db_path = 'sqlite:////app/catalog.db' #(for containerized env)

    # REMEMBER TO DO THE NEEDFUL BEFORE DEPLOYMENT!

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_PATH', ec2_db_path)
    app.config['JWT_ALGORITHM'] = 'HS256'
    app.config['JWT_VERIFY_SUB'] = False
    app.config['JWT_SECRET_KEY'] = 'xkG7Icv2lJ0rPiKfAqXZhVp1mE3Jt5NvYXQbC6MLo9I'  # Ensure a secure secret key


    # Initialize database with the app
    db.init_app(app)
    jwt = JWTManager(app)

    # print("find me... ")
    # print(app.config['SQLALCHEMY_DATABASE_URI'])

    from routes.product_routes import product_bp
    from routes.auth_routes import auth_bp
    from routes.user_routes import user_bp

 
    app.register_blueprint(product_bp, url_prefix='/api/v1')
    app.register_blueprint(auth_bp, url_prefix='/api/v1')
    app.register_blueprint(user_bp, url_prefix='/api/v1')
    

    @app.route('/api/v1/')
    def welcome():
        return jsonify({"message": "Welcome to the catalog!"})

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(host='0.0.0.0', port=5000)
    # venv/bin/watchmedo auto-restart --pattern="*.py" --recursive -- flask run