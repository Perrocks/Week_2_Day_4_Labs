import unittest
from src.phone_number import * 

class TestPhoneNumber(unittest.TestCase):
    
    def test_create_phone_number(self):
        phone_number = PhoneNumber(1234567890)
        result = phone_number.create_phone_number(phone_number)
        self.assertEqual("(123) 456-7890", result)

    