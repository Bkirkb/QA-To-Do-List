import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Tasks

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
                SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY = 'TEST_SECRET_KEY',
                DEBUG=True
            )
            return app

    def setUp(self):
        db.create_all()
        test_task = Tasks(description="Test the flask app")
        db.session.add(test_task)
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

     def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code, 200)
    
    def test_change_get(self):
        response = self.client.get(url_for('change'))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code, 200)
    
class TestRead(TestBase):
    def test_read_tasks(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"Test the flask app", response.data)
    
class TestCreate(TestBase):
    def test_create_task(self):
        response = self.client.post
            (url_for('create'),
            data=dict(description="Create a new task"),
            follow_redirects = True
            )
        self.assertIn(b"Create a new task", response.data)

class TestUpdate(TestBase):
    def test_update_task(self):
        response = self.client.post
            (url_for('update'),
            data=dict(description="Created task updated"),
            follow_redirects = True
            )
        self.assertIn(b"Create a new task", response.data)
