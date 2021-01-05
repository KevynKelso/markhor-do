import unittest

import sys
sys.path.append('../../markhor')
sys.path.append('../../markhor/app')

from app import app
app.testing = True

class RoutesTest(unittest.TestCase):
    def test_forward_slash_is_valid_route(self):
        with app.test_client() as client:
            response = client.post('/')

            self.assertEqual(response.status_code, 200)


    def test_test_is_valid_route(self):
        with app.test_client() as client:
            response = client.get('/test')

            self.assertEqual(response.status_code, 200)
        
        
    def test_test_fail_is_valid_route(self):
        with app.test_client() as client:
            response = client.get('/test-fail')

            self.assertEqual(response.status_code, 500)
