# from os import environ
# import json

# def getEnvironmentVariable(var_name):
    # if var_name not in environ:
        # raise KeyError(f'{var_name} environment variable is missing.')
    # else:
        # return environ[var_name]


# ENVIRONMENT = getEnvironmentVariable('ENVIRONMENT')
# DEFAULT_EMAIL = getEnvironmentVariable('DEFAULT_EMAIL')
# SENDER_EMAIL = getEnvironmentVariable('SENDER_EMAIL')
# SENDER_PASSWORD = getEnvironmentVariable('SENDER_PASSWORD')
# MARKHOR_ADMINS = json.loads(getEnvironmentVariable('MARKHOR_ADMINS'))
# SNIPCART_SECRET_API_KEY = getEnvironmentVariable('SNIPCART_SECRET_API_KEY')
import os

ENVIRONMENT = os.getenv('ENVIRONMENT')
DEFAULT_EMAIL = os.getenv('DEFAULT_EMAIL')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
MARKHOR_ADMINS = os.getenv('MARKHOR_ADMINS')
SNIPCART_SECRET_API_KEY = os.getenv('SNIPCART_SECRET_API_KEY')
