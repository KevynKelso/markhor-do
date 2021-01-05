from requests import HTTPError

from apis import sendToPymail


def handleKitsEmail(request_data, items_index):
    try:
        reservation_code = ''
        if len(request_data['content']['items'][items_index]['customFields']) > 0:
            if request_data['content']['items'][items_index]['customFields'][0]['name'] == "Reservation Code":
                reservation_code = request_data['content']['items'][items_index]['customFields'][0]['value']

        data = {
            "form_name": 'Kits Email',
            "sendto": 'Tara Burton',
            "invoice_number": request_data['content']['invoiceNumber'],
            "product": request_data['content']['items'][items_index]['name'],
            "description": request_data['content']['items'][items_index]['description'],
            "price": request_data['content']['items'][items_index]['totalPrice'],
            "quantity": request_data['content']['items'][items_index]['quantity'],
            "last4": request_data['content']['creditCardLast4Digits'],
            "reservation_code": reservation_code,
            "billing_name": request_data['content']['billingAddressName'],
            "email": request_data['content']['user']['email'],
            "billing_company_name": request_data['content']['billingAddressCompanyName'],
            "billing_address1": request_data['content']['billingAddressAddress1'],
            "billing_address2": request_data['content']['billingAddressAddress2'],
            "billing_city": request_data['content']['billingAddressCity'],
            "billing_state": request_data['content']['billingAddressProvince'],
            "billing_country": request_data['content']['billingAddressCountry'],
            "billing_zip": request_data['content']['billingAddressPostalCode'],
            "billing_phone": request_data['content']['billingAddressPhone'],
            "shipping_name": request_data['content']['shippingAddressName'],
            "shipping_company_name": request_data['content']['shippingAddressCompanyName'],
            "shipping_address1": request_data['content']['shippingAddressAddress1'],
            "shipping_address2": request_data['content']['shippingAddressAddress2'],
            "shipping_city": request_data['content']['shippingAddressCity'],
            "shipping_state": request_data['content']['shippingAddressProvince'],
            "shipping_country": request_data['content']['shippingAddressCountry'],
            "shipping_zip": request_data['content']['shippingAddressPostalCode'],
            "shipping_phone": request_data['content']['shippingAddressPhone']
        }

        response = sendToPymail(data)

        return response
    except (TypeError, HTTPError, KeyError):
        raise
