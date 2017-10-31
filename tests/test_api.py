# -*- coding: utf-8 -*-
""" Basic test classes. By no means complete but enough to give you an
idea on how to test. Coverage is not part of these tests but coverage
tests are handy for larger projects.
"""
import unittest
import json
import re
from base64 import b64encode
import os
import sys

from flask import url_for

"""Append the main project directory on the system path."""
BASEDIR = os.path.abspath(os.path.dirname(__file__))
PARENTDIR = os.path.join(BASEDIR, "..")
sys.path.append(BASEDIR)
sys.path.append(PARENTDIR)

from api import create_app

class APITestCase(unittest.TestCase):
    def setUp(self):
        """Set-up test case. Use the testing config."""
        self.app = create_app(config_name='testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        """Tear down test."""
        self.app_context.pop()

    def test_404(self):
        """Test if we get a 404 on a non existing page."""
        res = self.client.get('/nocando')
        self.assertEqual(res.status_code, 404)
        
    def test_home(self):
        """Test if we can reach the index page."""
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        
    def test_search_customer_wrong_method(self):
        """Test search for a customer with post instead of get."""
        res = self.client.post('http://localhost:5000/customers/')
        # Method post is not allowed on /customers
        self.assertEqual(res.status_code, 405) 
        
    def test_search_customer(self):
        """Test if the API can search for customers based on a partial
        name (GET request).
        
        """
        res = self.client.get('http://localhost:5000/customers/?search=A Company')
        self.assertEqual(res.status_code, 200)
        # We should have at least 1 customer namedd "A Company"
        self.assertIn('A Company', str(res.data))

    def test_get_custumer_info(self):
        """ We would need a dummy db with some test values to test this.
        Since this code is only meant as a short example, we will not
        include a sqlite database with test data. You could change this
        method to connect to your own test database.
        """
        res = self.client.get('http://localhost:5000/customers/info?search=A%20Company%20Two')
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        # We should have 1 customer "A Company Two"
        self.assertEqual('A Company Two', str(data["customer_id"]))
        
        res = self.client.get('http://localhost:5000/customers/info?search=A%20Company')
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        # We should have no customer info because there is more then
        # one customer with 'A Company' in the name.
        self.assertEqual(None, data)
        
        
# Make the tests executable
if __name__ == "__main__":
    unittest.main()
