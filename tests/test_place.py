#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_Place_inheritance(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_Place_attributes(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
