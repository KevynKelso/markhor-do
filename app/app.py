from flask import (
    Flask,
    request,
    redirect,
    render_template,
    abort,
    jsonify
)

import smtplib

import traceback
import logging
from logging.handlers import SMTPHandler

#import json
#import requests

from environment import (
    MARKHOR_ADMINS,
    SENDER_EMAIL,
    SENDER_PASSWORD
)

from functions import (
    loopThroughItems,
    validateSnipcartToken
)

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# ----------------------------------------------------------------------
# For limiting API traffic on all routes from an IP address.  For more advanced limiting we need Redis.
# ----------------------------------------------------------------------
limiter = Limiter(
    app,
    key_func=get_remote_address, default_limits=["200 per day", "50 per hour"]
)

# ----------------------------------------------------------------------
# APP CONFIGURATION SETTINGS
# ----------------------------------------------------------------------
app.config['ADMINS'] = MARKHOR_ADMINS

# ----------------------------------------------------------------------
# ERROR LOGGING with SMTP
# ----------------------------------------------------------------------
mail_handler = SMTPHandler(
    mailhost = ('smtp.office365.com', 587),
    fromaddr = SENDER_EMAIL,
    toaddrs = MARKHOR_ADMINS,
    subject = "Markhor Error",
    credentials = (SENDER_EMAIL, SENDER_PASSWORD),
    secure=()
)
mail_handler.setLevel(logging.ERROR)
app.logger.addHandler(mail_handler)


# ----------------------------------------------------------------------
# HTTP Routes
# ----------------------------------------------------------------------
@app.route('/', methods=['POST'])
def snipcartWebhook():
    if app.testing == True:
        return {'data': 'success'}, 200
    try:
        snipcart_request_token = request.headers.get('x-snipcart-requesttoken')

        if snipcart_request_token == None:
            raise KeyError('Invalid request: headers missing.')

        validateSnipcartToken(snipcart_request_token)

        request_data = request.get_json()

        if (request_data['eventName'] == 'order.completed'
            and 'items' in request_data['content']
        ):
            items = request_data['content']['items']

            loopThroughItems(items, request_data)

            return {'data': 'BSCS Snipcart order completed webhook.'}, 200

        return {'data': 'BSCS Snipcart no action taken.'}, 200
    except:
        app.logger.error(traceback.format_exc())
        return {'data': 'Internal Server Error'}, 500


@app.route('/test', methods=['GET'])
def test():
    return {'data': 'Test successful.'}, 200

@app.route('/test-fail', methods=['GET'])
def testFail():
    try:
        x = 10 / 0
        return {'data': 'Test successful.'}, 200
    except:
        app.logger.error(traceback.format_exc())
        return jsonify({'data': 'Internal Server Error'}), 500
