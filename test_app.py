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
        # TOKENS
        self.manager = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtwNE8walZuX2pjT0pJbTRJSFBlRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtaGFwcHlob3VyLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNzk0MjE1NzM5OTc0NTk0NTM1MiIsImF1ZCI6WyJmc25kY2Fwc3RvbmUiLCJodHRwczovL2ZzbmQtaGFwcHlob3VyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODg5Nzc0MzIsImV4cCI6MTU4OTA2MzgzMiwiYXpwIjoiclkzZWU2eGpvV29jWFA3UGtDVW91SFM0OHZYOVlBb28iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnJlc3RhdXJhbnQiLCJnZXQ6bG9naW4tcmVzdWx0cyIsImdldDptZW51X2l0ZW0iLCJnZXQ6cmVzdGF1cmFudCIsInBhdGNoOnJlc3RhdXJhbnQiLCJwb3N0OnJlc3RhdXJhbnQiXX0.fofDkMrRnL6CG6sOVj8aLLp5fF0WAkqi7sM4qcL_n3RrBDEKr8xf8exelgZlX3DVABwsMTD_ppD_lT2U8_FRieyoDAk7VXI8N0pxYp1Z39Hbff6jAzP-rQRzDD942a-O8A1hFlKH_HT0PiTSjExPYSoF5LR3cbyUaDeEZPOMZ5D61B-c87aZaAu9td9K5PiEFmxkjsdxaZXXxVIGc6IvyKDEHIkDYmtZX0baZmGMg10AM_4i4igk4HVP3TDiAL9-8ylwNVPCH1KKMDTtrecAMYFsFfLS2PcL-2WF6XsuJ8GE__dl6njYj6F8fMdq5vHWpPRu5s2u53dZRzIgaMGolA'
        self.customer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtwNE8walZuX2pjT0pJbTRJSFBlRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtaGFwcHlob3VyLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjA2OTg0MzEzMDkzMzEwMDI5MSIsImF1ZCI6WyJmc25kY2Fwc3RvbmUiLCJodHRwczovL2ZzbmQtaGFwcHlob3VyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODg5Nzc0ODgsImV4cCI6MTU4OTA2Mzg4OCwiYXpwIjoiclkzZWU2eGpvV29jWFA3UGtDVW91SFM0OHZYOVlBb28iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0OmxvZ2luLXJlc3VsdHMiLCJnZXQ6bWVudV9pdGVtIiwiZ2V0OnJlc3RhdXJhbnQiLCJwb3N0OnJlc2VydmF0aW9uIl19.GvJXDViLRCK1qrx_yl612Nc4B4xyKmW9Z8-0sh9xRGs8B1G6lalPsFlp1Ux5DGKZL9o1hy9qCS8GpfCzeIIm6E6DvCoS4L9NfkzIo-7eMxf_lPX-9xK8i-q2bC2yoMoqfyTZgHQ4ONlHm8BPAJg2K0qBIFMqN9erk0oLlfA1434Kv6IDH6ZaosLbUubNK4DWO4YScWvxauXGRzs5BnHYb2KC-NCvAvVysPZaEqhhIhk0FwWLqBNRlcXFuGhIkR_HvIoMmOmHAjORCWv8-lflp3F7yVXWEN0u3Ip9_3ZMgms1bWwjbe3FqWn_ZLL-DItdjc1KIHc4yycr4xR2Lzw_fw'
        self.badtoken = 'badtoken'
        
        # New Restaurant
        self.new_restaurant = {
            'name': 'Earls',
            'address': '5555 Street rd'
        }

        #Patch Restaurant
        self.change_restaurant_address = {
            'address': '1111 Street rd'
        }

        # Post New Reservations
        self.reservation_info = {
            'time_of_res': "2020-08-19 18:30:00",
            'num_of_people': 5,
            'name_for_res': "Reservations Name"
        }    

        #Add new restaurant if database is empty with good token and set current_rest_id
        if Restaurant.query.filter(Restaurant.owner_id != 'badtoken').count() == 0:
            res = self.client().post('/restaurants', headers={"Authorization": "Bearer {}".format(self.manager)}, json=self.new_restaurant)      
        self.current_rest_id = Restaurant.query.order_by(Restaurant.id.desc()).filter(Restaurant.owner_id != 'badtoken').first().id

        # add new restaurant with bad token is it doesnt exist, and set bad_rest_id
        if Restaurant.query.filter(Restaurant.owner_id == 'badtoken').count() == 0:
            bad_token_rest = Restaurant(name="Bad name", address="bad address", owner_id="badtoken")
            bad_token_rest.insert()
        self.bad_rest_id = Restaurant.query.filter(Restaurant.owner_id == 'badtoken').first().id
        

        

    def tearDown(self):
        """Executed after each test"""        
        pass



    # TESTS START HERE

    def test_homepage(self):       
        res = self.client().get('/')
        
        self.assertEqual(res.status_code, 200)


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


    
    def test_patch_restaurant_that_is_not_owners(self):               
        res = self.client().patch('/restaurants/' + str(self.bad_rest_id), headers={"Authorization": "Bearer {}".format(self.manager)}, json=self.change_restaurant_address)
                      
        self.assertEqual(res.status_code, 401)



    def test_patch_restaurant_that_does_not_exist(self):               
        res = self.client().patch('/restaurants/' + str(self.current_rest_id + 1000), headers={"Authorization": "Bearer {}".format(self.manager)}, json=self.change_restaurant_address)
                      
        self.assertEqual(res.status_code, 422)



    def test_post_reservation_with_vaild_customer(self):
        res = self.client().post('/restaurants/' + str(self.current_rest_id)  + '/reservation', headers={"Authorization": "Bearer {}".format(self.customer)}, json=self.reservation_info)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)



    def test_post_reservation_with_invaild_customer(self):
        res = self.client().post('/restaurants/' + str(self.current_rest_id)  + '/reservation', headers={"Authorization": "Bearer {}".format(self.badtoken)}, json=self.reservation_info)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)



    def test_post_reservation_with_non_existant_restaurant(self):
        res = self.client().post('/restaurants/' + str(self.current_rest_id + 1000)  + '/reservation', headers={"Authorization": "Bearer {}".format(self.customer)}, json=self.reservation_info)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)

    
    
    def test_delete_restaurant_with_valid_owner(self):
        res = self.client().delete('/restaurants/' + str(self.current_rest_id), headers={"Authorization": "Bearer {}".format(self.manager)})
        
        deleted_rest = Restaurant.query.get(self.current_rest_id)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(deleted_rest, None)



    def test_delete_non_existant_restaurant(self):
        res = self.client().delete('/restaurants/' + str((self.current_rest_id + 10000)), headers={"Authorization": "Bearer {}".format(self.manager)})
        
        deleted_rest = Restaurant.query.get(self.current_rest_id + 10000)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(deleted_rest, None)
    

    


if __name__ == "__main__":
    unittest.main()