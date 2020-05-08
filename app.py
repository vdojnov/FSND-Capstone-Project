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
      restaurants = Restaurant.query.order_by(Restaurant.id).all()
      res = [restaurant.format() for restaurant in restaurants]
    
    except:
      abort(422)

    return jsonify({
      'success': True,
      'restaurants': res
    })

  @app.route('/restaurants/<int:id>')
  def get_restaruants_by_id(id):
    try:
      restaurants = Restaurant.query.get(id)
      res = restaurants.format()
    
    except:
      abort(422)  

    return jsonify({
      'success': True,
      'restaurants': res
    })
  
  # Public - get:menu_item
  @app.route('/restaurants/<int:id>/menu')
  def get_restaruant_menu(id):
    r_id = id
    try:
      menu_items = MenuItems.query.filter(MenuItems.restaurant_id==r_id).all()
      if menu_items == []:
        return jsonify({
          'success': True,
          'message': 'No menu_items available'
        })
    except:
      abort(422)
    return jsonify({
      "items": [item.format() for item in menu_items],
      'success': True
    })

  
  # Customer - post:reservation
  @app.route('/restaurants/<int:id>/reservation', methods=['POST'])
  @requires_auth('post:reservation')
  def post_reservation(token, id):
    try:
      restaurant_id = id

      body = request.get_josn()
      time_of_res = body.get('time_of_res')
      num_of_people = body.get('num_of_people')
      name_for_res = body.get('name_for_res')

      customer_id = token.get('sub')

      reservation = Reservations(restaurant_id=restaurant_id, time_of_res=time_of_res, num_of_people=num_of_people, name_for_res=name_for_res, customer_id=customer_id)
      reservation.insert()

      upcoming_reservations = Reservations.query.filter(Reservations.customer_id==customer_id,time_of_res >= datetime.now())

    except:
      abort(403)

    return jsonify({
      'success': True,
      'upcoming_reservations': [reservation.format() for reservation in upcoming_reservations]
    })

  
  # Restaurant owner - post:restaurant
  @app.route('/restaurants', methods=['POST'])
  @requires_auth('post:restaurant')
  def post_restaurants(token):
    try:

      owner_id = token.get('sub')

      body = request.get_json()
      name = body.get('name')
      address = body.get('address')

      restaurant = Restaurant(owner_id=owner_id, name=name, address=address)
      restaurant.insert()

      users_restaurant = Restaurant.query.filter(Restaurant.owner_id==owner_id).all()

    except:
      abort(422)

    return jsonify({
      "owned_restaurants": [restaurant.format() for restaurant in users_restaurant],
      "success": True
    })


  # Restaurant owner - patch:restaurant
  @app.route('/restaurants/<int:id>', methods=['PATCH'])
  @requires_auth('patch:restaurant')
  def edit_restaurant(token, id):
    try:      
      rest_id = id
     
      owner_id = token.get('sub')
      
      restaurant = Restaurant.query.get(rest_id)
      
      if owner_id != restaurant.owner_id: 
        abort(401)
    # except 401:
    #   abort(401)  

    # try:       

      body = request.get_json()

      new_name = body.get('name')
      new_address = body.get('address')
  
      if new_name:
        restaurant.name = new_name
      if new_address:
        restaurant.address = new_address

      restaurant.update()

      updated_restaurant = Restaurant.query.get(rest_id)
    except:
      abort(422)
    return jsonify({
    "updated_restaurant": updated_restaurant.format(),
    "success": True
  })
    

  # Restaurant owner - delete:restaurant
  @app.route('/restaurants/<int:id>', methods=['DELETE'])
  @requires_auth('delete:restaurant')
  def delete_restaurant(token, id):
    try:
      owner_id = token.get('sub')

      restaurant = Restaurant.query.get(id)
      
      if owner_id != restaurant.owner_id:
        abort(401)

      restaurant.delete()
    except:
      abort(422)
    return jsonify({
      'success': True
    })


  @app.route('/login-results')
  @requires_auth('get:login-results')
  def login_results(token):
    user_token = token
  
    return jsonify({
      'token': user_token
    }) 



  # Error Handlers
  
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
                      "success": False,
                      "error": 422,
                      "message": "unprocessable"
                      }), 422


  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
      }), 404


  @app.errorhandler(401)
  def unauthorized(error):
      return jsonify({
          "success": False,
          "error": 401,
          "message": "Unauthorized Error"
      }), 401

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          "success": False,
          "error": 400,
          "message": "Bad Request"
      }), 400



  return app

app = create_app()

if __name__ == '__main__':
    app.run()