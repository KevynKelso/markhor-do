import base64


def validateParameterType(parameter, expected_type):
    try:
        if not isinstance(parameter, expected_type):
            raise TypeError(
                f'Invalid parameter type for parameter: {parameter}. '
                f'Received type {type(parameter)}. '
                f'Expected type {expected_type}.'
            )
    # added for catching TypeError raised by isinstance,
    # not self-raised TypeError, although it will catch that too
    except TypeError:
        raise
    

def encodeBase64(string):
    try:
        validateParameterType(string, str)
            
        encoded_utf8_string = base64.urlsafe_b64encode(string.encode('utf-8'))
        encoded_base64_string = str(encoded_utf8_string, 'utf-8')

        return encoded_base64_string
    except TypeError:
        raise


def getMissingFields(dict_obj, fields_list):
    try:
        validateParameterType(dict_obj, dict)
        validateParameterType(fields_list, list)
        missing_fields = []
        
        for field in fields_list:
            if field not in dict_obj:
                missing_fields.append(field)

        if len(missing_fields) == 0:
            return None
        else:
            return missing_fields
    except TypeError:
        raise
