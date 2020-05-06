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
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
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

# def test_create_new_actor_casting_assistant(self):

#     res = self.client().post('/actors', headers={"Authorization": "Bearer {}".format(self.casting_assistant)}, json=self.new_actor)
#     data = json.loads(res.data)

#     self.assertEqual(res.status_code, 401)
#     self.assertEqual(data['message'], {
#     'code': 'unauthorized', 
#     'description':'Permission not found.'})










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