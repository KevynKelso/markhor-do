from requests import HTTPError

from apis import sendToBojack
from utils import getMissingFields, validateParameterType


def getCanvasRegistrationRequiredFields():
    required_fields = [
        'email_address',
        'first_name',
        'last_name',
        'canvas_course_id'
    ]

    return required_fields


def handleCanvasRegistration(metadata):
    try:
        validateParameterType(metadata, dict)
        missing_fields = getMissingFields(metadata, getCanvasRegistrationRequiredFields())

        if missing_fields != None:
            raise ValueError('Missing required fields')

        canvas_course_id_as_int = int(metadata['canvas_course_id'])

        data = {
            'first_name': metadata['first_name'],
            'last_name': metadata['last_name'],
            'email_address': metadata['email_address'],
            'canvas_course_id': canvas_course_id_as_int
        }

        sendToBojack(data)
    # No KeyError b/c we're checking that in getMissingFields
    except (ValueError, HTTPError, TypeError):
        raise
