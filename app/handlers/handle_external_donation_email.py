from requests import HTTPError

from apis import sendToPymail

def handleExternalDonationEmail(request_data, items_index):
    try:
        data = {
            "sendto": 'Cameron Yee',
            "form_name": 'External Donation',
            "functions": ['sendExternalDonationEmail'],
            "donation_type": request_data['content']['items'][items_index]['name'],
            "name": request_data['content']['user']['billingAddressName'],
            "total_price": request_data['content']['items'][items_index]['totalPrice'],
            "date": request_data['createdOn'],
            "email": request_data['content']['user']['email']
        }

        response = sendToPymail(data)

        return response
    except (TypeError, HTTPError, KeyError):
        raise
