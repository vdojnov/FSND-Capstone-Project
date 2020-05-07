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
        
        # Test variables
        self.manager = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtwNE8walZuX2pjT0pJbTRJSFBlRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtaGFwcHlob3VyLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNzk0MjE1NzM5OTc0NTk0NTM1MiIsImF1ZCI6WyJmc25kY2Fwc3RvbmUiLCJodHRwczovL2ZzbmQtaGFwcHlob3VyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODg4MDYyMjMsImV4cCI6MTU4ODgxMzQyMywiYXpwIjoiclkzZWU2eGpvV29jWFA3UGtDVW91SFM0OHZYOVlBb28iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnJlc3RhdXJhbnQiLCJnZXQ6bWVudV9pdGVtIiwiZ2V0OnJlc3RhdXJhbnQiLCJwYXRjaDpyZXN0YXVyYW50IiwicG9zdDpyZXN0YXVyYW50Il19.RdehenvyxSns8UH03xEPpMVwSI55EBxjZK7UB3OCJXfIQI9MJhJh00WgOtr5s2kqC7UNdkUVrJ0fuGgVZ1Vuq_oqNknh0fyE4QlnDdc8ZBToqOK5O0icS8ln1HN6ofr7dsFdCIrbL20fHnJ5P9knhH_JEA2ZUQ6XYp_wMPifJ_IhjuPLl--kW2jCbtTz6KIAKmAp9Ki2NHoffVur_S1OeY0U6sLzV_KqcKNSX5GvBjvt098RHLNXbz4ULDJTJl4DAbKSSg1qewe72oIvelymcYEUOuzbMtPULFgNUFCBTEFSVumSuGCD0_JEJW_ECNUo8TyPhuHTjnDqxXeA3hPfoQ'
        self.customer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtwNE8walZuX2pjT0pJbTRJSFBlRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtaGFwcHlob3VyLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjA2OTg0MzEzMDkzMzEwMDI5MSIsImF1ZCI6WyJmc25kY2Fwc3RvbmUiLCJodHRwczovL2ZzbmQtaGFwcHlob3VyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODg4MDYzMTAsImV4cCI6MTU4ODgxMzUxMCwiYXpwIjoiclkzZWU2eGpvV29jWFA3UGtDVW91SFM0OHZYOVlBb28iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0Om1lbnVfaXRlbSIsImdldDpyZXN0YXVyYW50IiwicG9zdDpyZXNlcnZhdGlvbiJdfQ.ghQjDCC4InpE3rUZ4NwpHps55jGVwu_Agw8163bmyMeQ-sErEf4twKw8HhXB8aYISDu17YFRs77i5uTmaiialW0jCNLdGzumlGtEgqcAgKQU9Y_QE60VRtnTw442XSAhtFf-okwdgopzgSqH06eKBR1ZrqsMKEg9LcQsT6MafbW4DmHTqLsQvXd4Af1e44QHOwBGWFZk8dAP-5Tg9xYSLK6jItXTT_i4vjFFn8Xak44Kr9qnKbzhfFF8xLa74QcG0jiYgBgWLlaXetoUzbKNdWdQ-vXqveflBkSWvjjvcpZ-rVvYmP2EYgmw4VW_pzLWOUf6cfVd1ATD5cIJOKAiqg'
        self.badtoken = 'badtoken'

        self.new_restaurant = {
            'name': 'Earls',
            'address': '5555 Street rd'
        }


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

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_homepage(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_get_restaurants_empty_db(self):
        res = self.client().get('/restaurants')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], 'No restaurants available')


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

        restaurants = Restaurant.query.all()
        output = [restaurant.format() for restaurant in restaurants]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # self.assertEqual(data['restaurants'], output)



    # def test_get_menu_items(self):
    #     res = self.client().get('/restaurants')
    #     self.assertEqual(res.status_code, 200)


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