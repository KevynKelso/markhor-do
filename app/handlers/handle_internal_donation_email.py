from requests import HTTPError

from apis import sendToPymail


def handleInternalDonationEmail(request_data, items_index):
    try:
        in_memory_slash_honor_of = None
        if len(request_data['content']['items'][items_index]['customFields']) == 1:
            in_memory_slash_honor_of = (
                request_data['content']['items'][items_index]['customFields'][0]['value']
            )

        data = {
            "sendto": ['Lauren Novo', 'Aleigh Raffelson', 'Valerie Maltese'],
            "form_name": 'Internal Donation',
            "invoice_number": request_data['content']['invoiceNumber'],
            "donation_type": request_data['content']['items'][items_index]['name'],
            "name": request_data['content']['user']['billingAddressName'],
            "email": request_data['content']['user']['email'],
            "in_memory_slash_honor_of": in_memory_slash_honor_of,
            "total_price": request_data['content']['items'][items_index]['totalPrice'],
            "billing_name": request_data['content']['billingAddressName'],
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
