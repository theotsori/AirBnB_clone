#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_City_inherits_from_BaseModel(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_City_has_state_id_attribute(self):
        self.assertTrue(hasattr(self.city, 'state_id'))

    def test_City_has_name_attribute(self):
        self.assertTrue(hasattr(self.city, 'name'))

    def test_City_state_id_is_empty_string(self):
        self.assertEqual(self.city.state_id, '')

    def test_City_name_is_empty_string(self):
        self.assertEqual(self.city.name, '')

if __name__ == '__main__':
    unittest.main()
