from flask_sqlalchemy import SQLAlchemy

from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(2083), nullable=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)