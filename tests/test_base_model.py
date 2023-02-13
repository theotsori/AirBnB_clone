#!/usr/bin/python3

import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_base_model_instance(self):
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)

    def test_base_model_id(self):
        b = BaseModel()
        self.assertIsInstance(b.id, str)
        self.assertEqual(len(b.id), 36)

    def test_base_model_created_at(self):
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime)

    def test_base_model_updated_at(self):
        b = BaseModel()
        self.assertIsInstance(b.updated_at, datetime)
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_base_model_to_dict(self):
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIsInstance(b_dict, dict)
        self.assertEqual(b_dict['__class__'], 'BaseModel')
        self.assertEqual(b_dict['id'], b.id)
        self.assertEqual(b_dict['created_at'], b.created_at.isoformat())
        self.assertEqual(b_dict['updated_at'], b.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
