#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity_instance(self):
        a = Amenity()
        self.assertIsInstance(a, Amenity)
        self.assertIsInstance(a, BaseModel)

    def test_amenity_name(self):
        a = Amenity()
        a.name = "Wi-Fi"
        self.assertEqual(a.name, "Wi-Fi")


if __name__ == '__main__':
    unittest.main()
