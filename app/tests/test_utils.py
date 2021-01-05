import unittest

from base64 import b64decode
import binascii

from utils import (
    encodeBase64,
    getMissingFields,
    validateParameterType
)
    
class UtilsTest(unittest.TestCase):
    def test_encodeBase64_returns_a_string(self):
        string = 'test+/i='

        result = encodeBase64(string)

        try:
            b64decode(result)
        except binascii.Error:
            raise
            

    def test_encodeBase64_raises_an_error_if_the_parameter_is_a_number(self):
        self.assertRaises(TypeError, encodeBase64, 1)


    def test_encodeBase64_raises_an_error_if_the_parameter_is_a_dictionary(self):
        self.assertRaises(TypeError, encodeBase64, {'test': 1})

        
    def test_encodeBase64_raises_an_error_if_the_parameter_is_a_boolean(self):
        self.assertRaises(TypeError, encodeBase64, True)


    def test_getMissingFields_wrong_parameter_dict_type(self):
        self.assertRaises(TypeError, getMissingFields, 'test', 'test')

        
    def test_getMissingFields_wrong_parameter_list_type(self):
        self.assertRaises(TypeError, getMissingFields, {'test': 1}, 'test')

        
    def test_getMissingFields_no_missing_fields(self):
        self.assertIsNone(getMissingFields({'test': 1}, ['test']))

        
    def test_getMissingFields_missing_fields(self):
        missing_fields = getMissingFields({'test': 1}, ['foo', 'bar'])
        self.assertEqual(missing_fields[0], 'foo')
        self.assertEqual(missing_fields[1], 'bar')
        self.assertEqual(len(missing_fields), 2)


    def test_validateParameterType_throws_type_error(self):
        self.assertRaises(TypeError, validateParameterType, 'test', int)
        self.assertRaises(TypeError, validateParameterType, 0, str)
        self.assertRaises(TypeError, validateParameterType, {'test': 0}, str)
        self.assertRaises(TypeError, validateParameterType, {'test': 0}, list)
        
        
    def test_validateParameterType_returns_none_on_success(self):
        self.assertIsNone(validateParameterType('test', str))
        self.assertIsNone(validateParameterType(0, int))
        self.assertIsNone(validateParameterType([0], list))
        self.assertIsNone(validateParameterType({'test': 0}, dict))
