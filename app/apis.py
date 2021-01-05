import requests
from utils import validateParameterType


def sendToPymail(fields):
    try:
        validateParameterType(fields, dict)

        url = 'https://pymail.bscs.org/form'
        response = requests.post(url=url, json=fields)

        if response.status_code == 400:
            raise requests.HTTPError(
                f'Error from Pymail: {response.json()["message"]}')

        return response
    except (TypeError, requests.HTTPError):
        raise


def sendToBojack(fields):
    try:
        validateParameterType(fields, dict)

        url = 'https://bojack.bscs.org/enroll-in-course'
        response = requests.post(url=url, json=fields)

        if response.status_code == 400:
            raise requests.HTTPError(
                f'Error from Bojack: {response.json()["message"]}')

        return response
    except (TypeError, requests.HTTPError):
        raise
