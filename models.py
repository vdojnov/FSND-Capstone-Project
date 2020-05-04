
from sqlalchemy import Column, String, create_engine, Integer, DateTime, Numeric, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

# Table to store information about the restaurants
class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    owner_id = Column(String)  # owner_id will be retrieved from token to see which user owns the restaurant
    reservation_rel = db.relationship('Reservations', backref='restaurnt_res', lazy=True)
    reservation_rel = db.relationship('MenuItems', backref='restaurnt_menu_item', lazy=True)    

# Table to store information about the reservations at restaurants
class Reservations(db.Model):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    time_of_res = Column(DateTime)
    num_of_people = Column(Integer)
    name_for_res = Column(String) 
    customer_id = Column(String) # customer_id will be retrieved from token
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

# Table to store information about the Menu Items at restaurants
class MenuItems(db.Model):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Numeric)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    


