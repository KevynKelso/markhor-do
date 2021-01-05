import unittest
import os

# B/c coverage doesn't include these in sys.path
import sys
sys.path.append('../../pymail')
sys.path.append('../../pymail/app')

from app import app
from environment import getEnvironmentVariable


app.testing = True

# Don't write out ENV Variables anywhere
class EnvironmentVariableTest(unittest.TestCase):
    def test_success_default_email(self):
        DEFAULT_EMAIL = getEnvironmentVariable('DEFAULT_EMAIL')

        self.assertIsNotNone(DEFAULT_EMAIL)
        self.assertTrue(isinstance(DEFAULT_EMAIL, str))


    def test_success_environment(self):
        ENVIRONMENT = getEnvironmentVariable('ENVIRONMENT')

        self.assertIsNotNone(ENVIRONMENT)
        self.assertTrue(isinstance(ENVIRONMENT, str))


    def test_success_sender_email(self):
        SENDER_EMAIL = getEnvironmentVariable('SENDER_EMAIL')

        self.assertIsNotNone(SENDER_EMAIL)
        self.assertTrue(isinstance(SENDER_EMAIL, str))


    def test_success_sender_password(self):
        SENDER_PASSWORD = getEnvironmentVariable('SENDER_PASSWORD')

        self.assertIsNotNone(SENDER_PASSWORD)
        self.assertTrue(isinstance(SENDER_PASSWORD, str))


    def test_success_snipcart_secret_api_key(self):
        SNIPCART_SECRET_API_KEY = getEnvironmentVariable('SNIPCART_SECRET_API_KEY')

        self.assertIsNotNone(SNIPCART_SECRET_API_KEY)
        self.assertTrue(isinstance(SNIPCART_SECRET_API_KEY, str))


    def test_success_markhor_admins(self):
        MARKHOR_ADMINS = getEnvironmentVariable('MARKHOR_ADMINS')

        self.assertIsNotNone(MARKHOR_ADMINS)
        self.assertTrue(isinstance(MARKHOR_ADMINS, str))


    def test_key_does_not_exist(self):
        self.assertRaises(KeyError, getEnvironmentVariable, 'FALSE_KEY')


if __name__ == '__main__':
    unittest.main()
