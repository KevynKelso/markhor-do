import unittest
from unittest.mock import patch

from handlers.handle_canvas_registration import (
    getCanvasRegistrationRequiredFields,
    handleCanvasRegistration
)

from handlers.handle_external_donation_email import (
    handleExternalDonationEmail
)

from handlers.handle_internal_donation_email import (
    handleInternalDonationEmail
)

from handlers.handle_kits_email import (
    handleKitsEmail
)

from handlers.handle_pymail import (
    handlePymail
)


class HandlersTest(unittest.TestCase):
    def test_getCanvasRegistrationRequiredFields_success(self):
        result = getCanvasRegistrationRequiredFields()

        self.assertEqual(len(result), 4)

    def test_handleCanvasRegistration_raises_type_error(self):
        self.assertRaises(TypeError, handleCanvasRegistration, ['test'])
        self.assertRaises(TypeError, handleCanvasRegistration, 'test')
        self.assertRaises(TypeError, handleCanvasRegistration, 1)

    def test_handleCanvasRegistration_raises_value_error(self):
        self.assertRaises(ValueError, handleCanvasRegistration, {'test': True})

    def test_handleCanvasRegistration_successful(self):
        with patch('apis.requests.post') as mock_post:
            mock_post.return_value.status_code = 200

            data = {
                'email_address': 'test',
                'first_name': 'test',
                'last_name': 'test',
                'canvas_course_id': 1
            }

            handleCanvasRegistration(data)

            assert mock_post.called

    def test_handleExternalDonationEmail_raises_value_error(self):
        data = {
            'test': True
        }

        self.assertRaises(KeyError, handleExternalDonationEmail, data, 0)

    def test_handleExternalDonationEmail_success(self):
        with patch('apis.requests.post') as mock_post:
            mock_post.return_value.status_code = 200

            data = {
                'content': {
                    'items': [{'name': 'test', 'totalPrice': 0}],
                    'user': {
                        'email': 'test',
                        'billingAddressName': 'test'
                    }
                },
                'createdOn': 'test'
            }

            handleExternalDonationEmail(data, 0)

            assert mock_post.called

    def test_handleInternalDonationEmail_raises_value_error(self):
        data = {
            'test': True
        }

        self.assertRaises(KeyError, handleInternalDonationEmail, data, 0)

    def test_handleInternalDonationEmail_success(self):
        with patch('apis.requests.post') as mock_post:
            mock_post.return_value.status_code = 200

            data = {
                'content': {
                    'items': [{'name': 'test', 'totalPrice': 0, 'customFields': []}],
                    'user': {
                        'email': 'test',
                        'billingAddressName': 'test'
                    },
                    'invoiceNumber': 1,
                    'billingAddressName': 'test',
                    'billingAddressCompanyName': 'test',
                    'billingAddressAddress1': 'test',
                    'billingAddressAddress2': 'test',
                    'billingAddressCity': 'test',
                    'billingAddressProvince': 'test',
                    'billingAddressCountry': 'test',
                    'billingAddressPostalCode': 'test',
                    'billingAddressPhone': 'test',
                    'shippingAddressName': 'test',
                    'shippingAddressCompanyName': 'test',
                    'shippingAddressAddress1': 'test',
                    'shippingAddressAddress2': 'test',
                    'shippingAddressCity': 'test',
                    'shippingAddressProvince': 'test',
                    'shippingAddressCountry': 'test',
                    'shippingAddressPostalCode': 'test',
                    'shippingAddressPhone': 'test',
                },
                'createdOn': 'test'
            }

            handleInternalDonationEmail(data, 0)

            assert mock_post.called

    def test_handleKitsEmail_raises_value_error(self):
        data = {
            'test': True
        }

        self.assertRaises(KeyError, handleKitsEmail, data, 0)

    def test_handleKitsEmail_success(self):
        with patch('apis.requests.post') as mock_post:
            mock_post.return_value.status_code = 200

            data = {
                'content': {
                    'items': [
                        {
                            'name': 'test',
                            'totalPrice': 0,
                            'description': 'test',
                            'price': 'price',
                            'quantity': 1,
                            'customFields': []
                        }],
                    'user': {
                        'email': 'test',
                        'billingAddressName': 'test'
                    },
                    'creditCardLast4Digits': 1234,
                    'invoiceNumber': 1,
                    'billingAddressName': 'test',
                    'billingAddressCompanyName': 'test',
                    'billingAddressAddress1': 'test',
                    'billingAddressAddress2': 'test',
                    'billingAddressCity': 'test',
                    'billingAddressProvince': 'test',
                    'billingAddressCountry': 'test',
                    'billingAddressPostalCode': 'test',
                    'billingAddressPhone': 'test',
                    'shippingAddressName': 'test',
                    'shippingAddressCompanyName': 'test',
                    'shippingAddressAddress1': 'test',
                    'shippingAddressAddress2': 'test',
                    'shippingAddressCity': 'test',
                    'shippingAddressProvince': 'test',
                    'shippingAddressCountry': 'test',
                    'shippingAddressPostalCode': 'test',
                    'shippingAddressPhone': 'test',
                },
                'createdOn': 'test'
            }

            handleKitsEmail(data, 0)

            assert mock_post.called

    def test_handlePymail_success(self):
        with patch('apis.requests.post') as mock_post:
            mock_post.return_value.status_code = 200

            metadata = {
                'sendto': ['test']
            }

            data = {
                'content': {
                    'items': [
                        {
                            'name': 'test',
                            'totalPrice': 0,
                            'description': 'test',
                            'price': 'price',
                            'quantity': 1,
                            'customFields': []
                        }],
                    'user': {
                        'email': 'test',
                        'billingAddressName': 'test'
                    },
                    'creditCardLast4Digits': 1234,
                    'invoiceNumber': 1,
                    'billingAddressName': 'test',
                    'billingAddressCompanyName': 'test',
                    'billingAddressAddress1': 'test',
                    'billingAddressAddress2': 'test',
                    'billingAddressCity': 'test',
                    'billingAddressProvince': 'test',
                    'billingAddressCountry': 'test',
                    'billingAddressPostalCode': 'test',
                    'billingAddressPhone': 'test',
                    'shippingAddressName': 'test',
                    'shippingAddressCompanyName': 'test',
                    'shippingAddressAddress1': 'test',
                    'shippingAddressAddress2': 'test',
                    'shippingAddressCity': 'test',
                    'shippingAddressProvince': 'test',
                    'shippingAddressCountry': 'test',
                    'shippingAddressPostalCode': 'test',
                    'shippingAddressPhone': 'test',
                },
                'createdOn': 'test'
            }

            handlePymail('test', 0, metadata, data)

            assert mock_post.called
