from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

# Dynamically set database path based on environment
ec2_db_path = 'sqlite://///home/ali/all-dev/PHASE-2/AWS/flask_app/catalog.db'
# ec2_db_path = 'sqlite:////home/ubuntu/catalog_server/catalog.db'
# REMEMBER TO DO THE NEEDFUL BEFORE DEPLOYMENT!

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_PATH', ec2_db_path)
print("find me... ")
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)

@app.route('/api/v1/products', methods=['GET'])
def get_products():
    products = Products.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'price': p.price
    } for p in products])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)