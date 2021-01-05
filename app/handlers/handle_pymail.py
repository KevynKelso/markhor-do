from copy import deepcopy

from requests import HTTPError

from apis import sendToPymail


def handlePymail(item_id, items_index, metadata, request_data):
    try:
        data = {
            "form_name": "BSCS Website Payment Form",
            "sendto": metadata['sendto'],
            "invoice_number": request_data['content']['invoiceNumber'],
            "product": request_data['content']['items'][items_index]['name'],
            "description": request_data['content']['items'][items_index]['description'],
            "price": request_data['content']['items'][items_index]['totalPrice'],
            "quantity": request_data['content']['items'][items_index]['quantity'],
            "last4": request_data['content']['creditCardLast4Digits'],
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

        metadata_deepcopy = deepcopy(metadata)
        # avoids side effects to original metadata dict
        del metadata_deepcopy['sendto']

        # add any metadata fields to data besides sendto field
        data.update(metadata_deepcopy)

        customFields = request_data['content']['items'][items_index]['customFields']
        for field in customFields:
            data[field['name']] = field['displayValue']

        response = sendToPymail(data)

        return response
    except (TypeError, HTTPError, KeyError, ValueError):
        raise
