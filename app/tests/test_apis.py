import requests
import unittest
from unittest.mock import patch

from apis import sendToPymail, sendToBojack


class ApisTest(unittest.TestCase):
    def test_sendToPymail_success(self):
        with patch('apis.requests.post') as mock_post:
            mock_post.return_value.status_code = 200

            pymail_response = sendToPymail({'test': True})

            assert mock_post.called
            self.assertEqual(pymail_response.status_code, 200)


    def test_sendToPymail_fail(self):
        with patch('apis.requests.post') as mock_post:
            mock_post.return_value.status_code = 400
            mock_post.json.return_value = {'message': 'Test Error'}

            with self.assertRaises(requests.HTTPError) as cm:
                response = sendToPymail({'test': True})
                self.assertEqual(response.json()['message'] == 'Test Error')

                
    def test_sendToBojack_success(self):
        with patch('apis.requests.post') as mock_post:
            mock_post.return_value.status_code = 200

            bojack_response = sendToBojack({'test': True})

            assert mock_post.called
            self.assertEqual(bojack_response.status_code, 200)


    def test_sendToBojack_fail(self):
        with patch('apis.requests.post') as mock_post:
            mock_post.return_value.status_code = 400
            mock_post.json.return_value = {'message': 'Test Error'}

            with self.assertRaises(requests.HTTPError) as cm:
                response = sendToBojack({'test': True})
                self.assertEqual(response.json()['message'] == 'Test Error')
