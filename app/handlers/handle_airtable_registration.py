from requests import HTTPError

from apis import sendToPymail


def handleAirtableRegistration(item_id, metadata):
    try:
        alternate_phone = None
        others = None

        if 'alternatePhone' in metadata:
            alternate_phone = metadata['alternatePhone']

        if 'others' in metadata:
            others = metadata['others']

        data = {
            'form_name': 'Airtable Registration',
            'event_name': item_id.replace('-', ' '),
            # 'sendto': metadata['sendto'],
            'sendto': ['Cameron Yee', 'Jillian Nickerson'],
            'first_name': metadata['firstname'],
            'last_name': metadata['lastname'],
            'email': metadata['email'],
            'phone': metadata['phone'],
            'alternate_phone': alternate_phone,
            'organization': metadata['organization'],
            'street': metadata['street'],
            'city': metadata['city'],
            'state': metadata['addressstate'],
            'zipcode': metadata['zipcode'],
            'others': others
        }

        response = sendToPymail(data)

        return response
    except (TypeError, HTTPError, KeyError):
        raise
