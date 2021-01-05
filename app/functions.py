import json
import requests

from handlers.handle_airtable_registration import handleAirtableRegistration
from handlers.handle_canvas_registration import handleCanvasRegistration
from handlers.handle_external_donation_email import handleExternalDonationEmail
from handlers.handle_internal_donation_email import handleInternalDonationEmail
from handlers.handle_kits_email import handleKitsEmail
from handlers.handle_pymail import handlePymail

from environment import SNIPCART_SECRET_API_KEY

from utils import encodeBase64, validateParameterType

import inspect


def callItemFunction(item, items_index, request_data):
    try:
        if item['metadata'] and isinstance(item['metadata'], str):
            item['metadata'] = json.loads(item['metadata'])

        if item['metadata'] and 'sendto' in item['metadata']:
            handlePymail(item['id'], items_index,
                         item['metadata'], request_data)

        if item['metadata'] and 'vista' in item['id']:
            handleCanvasRegistration(item['metadata'])

        # Metadata will be "sendto" when donation is set up and null on recurring charges
        if item['metadata'] and 'donation' in item['id'].lower():
            handleExternalDonationEmail(request_data, items_index)
    except (ValueError, requests.HTTPError, TypeError, KeyError):
        raise


def loopThroughItems(items, request_data):
    try:
        validateParameterType(items, list)
        validateParameterType(request_data, dict)

        for index, item in enumerate(items):
            callItemFunction(item, index, request_data)
    except TypeError:
        raise


def validateSnipcartToken(snipcart_request_token):
    validation_url = f'https://app.snipcart.com/api/requestvalidation/{snipcart_request_token}'

    skey = SNIPCART_SECRET_API_KEY or 'test'
    encoded_base64_string = encodeBase64(SNIPCART_SECRET_API_KEY)

    validation_headers = {
        "Authorization": f"Basic {encoded_base64_string}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.get(url=validation_url, headers=validation_headers)

    response_json = response.json()

    try:
        if response_json == None:
            raise requests.HTTPError('Invalid request: response not json.')
        elif response.status_code != 200:
            raise requests.HTTPError(
                f'Invalid request: Snipcart returned status {response.status_code}')
        elif response_json['token'] != snipcart_request_token:
            raise ValueError('Invalid request: invalid token.')
        else:
            return True
    except (TypeError, requests.HTTPError, ValueError):
        print(inspect.trace()[-1][0].f_locals['response_json'])
        raise
