import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Restaurant, Reservations, MenuItems


class FsndCapstoneTestCase(unittest.TestCase):
    
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
                
        # Test database name
        self.database_name = "fsndcapstone_test"
        self.database_path = "postgresql://postgres:viktor@localhost:5432/" + self.database_name
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()



        # Test variables
        self.manager = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtwNE8walZuX2pjT0pJbTRJSFBlRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtaGFwcHlob3VyLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNzk0MjE1NzM5OTc0NTk0NTM1MiIsImF1ZCI6WyJmc25kY2Fwc3RvbmUiLCJodHRwczovL2ZzbmQtaGFwcHlob3VyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODg5MTM1OTksImV4cCI6MTU4ODkyMDc5OSwiYXpwIjoiclkzZWU2eGpvV29jWFA3UGtDVW91SFM0OHZYOVlBb28iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnJlc3RhdXJhbnQiLCJnZXQ6bG9naW4tcmVzdWx0cyIsImdldDptZW51X2l0ZW0iLCJnZXQ6cmVzdGF1cmFudCIsInBhdGNoOnJlc3RhdXJhbnQiLCJwb3N0OnJlc3RhdXJhbnQiXX0.Le25kEl_C5wZX31MCGw5UsIOS0tbxLyhThHd7gSm36O3JwJsrjh52T25BOcClrKd9spnY3W-fmKwV7KTmlXApN3GVJNX4BSyAZTE1wtHTI3Lak89Pvi6ddJ27mneuJCv7x1zbSLD9qkpsA7VhX1D2FeD31fMUbyITzFxOCVE3E0yQZrAyPFYC3NfroPbVaque8M8yF7xwNF11Mt9TwHNqdyo1OA7ezLp1CjT8Kmi5jOcnnDcgFr8p8jx-1BOazBzQKCCKQeL8NiKb_ROYCvf_1UyNa2u33yhfrFXs6tquvaaZAct187lh7EvGEVhVkcqjC7jfBgQWJro0eL1yr9GcQ'
        self.customer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtwNE8walZuX2pjT0pJbTRJSFBlRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtaGFwcHlob3VyLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjA2OTg0MzEzMDkzMzEwMDI5MSIsImF1ZCI6WyJmc25kY2Fwc3RvbmUiLCJodHRwczovL2ZzbmQtaGFwcHlob3VyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODg4MDYzMTAsImV4cCI6MTU4ODgxMzUxMCwiYXpwIjoiclkzZWU2eGpvV29jWFA3UGtDVW91SFM0OHZYOVlBb28iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0Om1lbnVfaXRlbSIsImdldDpyZXN0YXVyYW50IiwicG9zdDpyZXNlcnZhdGlvbiJdfQ.ghQjDCC4InpE3rUZ4NwpHps55jGVwu_Agw8163bmyMeQ-sErEf4twKw8HhXB8aYISDu17YFRs77i5uTmaiialW0jCNLdGzumlGtEgqcAgKQU9Y_QE60VRtnTw442XSAhtFf-okwdgopzgSqH06eKBR1ZrqsMKEg9LcQsT6MafbW4DmHTqLsQvXd4Af1e44QHOwBGWFZk8dAP-5Tg9xYSLK6jItXTT_i4vjFFn8Xak44Kr9qnKbzhfFF8xLa74QcG0jiYgBgWLlaXetoUzbKNdWdQ-vXqveflBkSWvjjvcpZ-rVvYmP2EYgmw4VW_pzLWOUf6cfVd1ATD5cIJOKAiqg'
        self.badtoken = 'badtoken'

        self.new_restaurant = {
            'name': 'Earls',
            'address': '5555 Street rd'
        }

        self.change_restaurant_address = {
            'address': '1111 Street rd'
        }

        if Restaurant.query.count() == 0:
            res = self.client().post('/restaurants', headers={"Authorization": "Bearer {}".format(self.manager)}, json=self.new_restaurant)
            
       
        self.current_rest_id = Restaurant.query.order_by(Restaurant.id.desc()).first().id

        

    def tearDown(self):
        """Executed after each test"""        
        pass












    def test_homepage(self):       
        res = self.client().get('/')
        
        self.assertEqual(res.status_code, 200)

    # def test_get_restaurants_empty_db(self):
    #     res = self.client().get('/restaurants')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['restaurants'], [])


    def test_post_restaurant_with_valid_token(self):        
        res = self.client().post('/restaurants', headers={"Authorization": "Bearer {}".format(self.manager)}, json=self.new_restaurant)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_401_post_restaurant_with_invalid_token(self):        
        res = self.client().post('/restaurants', headers={"Authorization": "Bearer {}".format(self.badtoken)}, json=self.new_restaurant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
    


    def test_get_restaurants(self):        
        res = self.client().get('/restaurants')
        data = json.loads(res.data)

        restaurants = Restaurant.query.order_by(Restaurant.id).all()        
        output = [restaurant.format() for restaurant in restaurants]
       

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['restaurants'], output)



    def test_get_restaurant_by_id(self):        
        res = self.client().get('/restaurants/' + str(self.current_rest_id))
        data = json.loads(res.data)

        restaurant = Restaurant.query.get(self.current_rest_id)
        format_rest = restaurant.format()
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['restaurants'], format_rest)



    def test_patch_restaurant_by_id(self):               
        res = self.client().patch('/restaurants/' + str(self.current_rest_id), headers={"Authorization": "Bearer {}".format(self.manager)}, json=self.change_restaurant_address)
        data = json.loads(res.data)
        

        restaurant = Restaurant.query.get(self.current_rest_id)
        format_rest = restaurant.format()
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['updated_restaurant']['address'], self.change_restaurant_address['address'])

    


    # def test_patch_restaurant_by_id(self):               
    #     res = self.client().patch('/restaurants/55', headers={"Authorization": "Bearer {}".format(self.manager)}, json=self.change_restaurant_address)
                      
    #     self.assertEqual(res.status_code, 422)
        



















    # def test_create_new_actor_casting_assistant(self):

    #     res = self.client().post('/restaurnats', headers={"Authorization": "Bearer {}".format(self.casting_assistant)}, json=self.new_actor)
    #     data = json.loads(res.data)

    #     res = Restaurant(name="res", address='addressssss', owner_id='owner idddd')
    #     res.insert()

    #     self.assertEqual(res.status_code, 401)
    #     self.assertEqual(data['message'], {
    #     'code': 'unauthorized', 
    #     'description':'Permission not found.'})




if __name__ == "__main__":
    unittest.main()





# def test_create_new_movies_executive_producer(self):

#     res = self.client().post('/movies',
#     headers={
#     "Authorization": "Bearer {}".format(
#     self.executive_producer)
#     }, json=self.movies)
#     data = json.loads(res.data)

#     self.assertEqual(res.status_code, 200)
#     self.assertEqual(data['success'], True)

# def test_create_new_movies_casting_assistant(self):

#     res = self.client().post('/movies',
#     headers={
#     "Authorization": "Bearer {}".format(
#     self.casting_assistant)
#     }, json=self.movies)
#     data = json.loads(res.data)

#     self.assertEqual(res.status_code, 401)
#     self.assertEqual(data['message'], {
#         'code': 'unauthorized', 
#         'description': 'Permission not found.'
#         })