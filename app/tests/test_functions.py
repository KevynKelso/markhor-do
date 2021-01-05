import requests
import unittest
from unittest.mock import patch

from functions import validateSnipcartToken


class FunctionsTest(unittest.TestCase):
    # BROKEN TEST
    # def test_validateSnipcartToken_success(self):
    #     with patch('functions.requests.get') as mock_get:
    #         mock_get.return_value.status_code = 200
    #         mock_get.json.return_value = {'token': 'test'}

    #         response = validateSnipcartToken('test')
    #         print(response)

    #         self.assertEqual(response, True)

    # BROKEN TEST
    # def test_validateSnipcartToken_no_json_in_response(self):
    #     with patch('functions.requests.get') as mock_get:
    #         mock_get.return_value.status_code = 200
    #         mock_get.json.return_value = None
    #         self.assertRaises(requests.HTTPError, validateSnipcartToken, 'test')

    def test_validateSnipcartToken_not_200(self):
        with patch('functions.requests.get') as mock_get:
            mock_get.return_value.status_code = 400
            self.assertRaises(requests.HTTPError,
                              validateSnipcartToken, 'test')

    def test_validateSnipcartToken_invalid_token(self):
        with patch('functions.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {'token': 'nottest'}
            self.assertRaises(ValueError, validateSnipcartToken, 'test')
