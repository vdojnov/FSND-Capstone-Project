# .\env\Scripts\activate

import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Reservations, Restaurant, MenuItems
from auth.auth import requires_auth
# from auth.auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.route('/')
  def get_greeting():
    return "Hello, welcome to my FSND Capstone project! Be sure to read the README.md file in the repo for testing instructions."

  # Public - get:restaurant
  @app.route('/restaurants')
  def get_restaruants():
    try:
      restaurants = Restaurant.query.all()
    except:
      abort(403)
    return jsonify([restaurant.format() for restaurant in restaurants])

  # Public - get:menu_item
  # @app.route('/')

  # Public - get:restaurant

  # Customer - post:reservation

  # Restaurant owner - post:restaurant

  # Restaurant owner - patch:restaurant

  # Restaurant owner - delete:restaurant

  



  return app

app = create_app()

if __name__ == '__main__':
    app.run()