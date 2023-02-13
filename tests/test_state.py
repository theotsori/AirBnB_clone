#!/usr/bin/python3

import unittest
import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_attributes(self):
        self.assertHasAttr(self.state, "name")
        self.assertHasAttr(self.state, "created_at")
        self.assertHasAttr(self.state, "updated_at")
        self.assertHasAttr(self.state, "id")

    def test_type(self):
        self.assertIsInstance(self.state.name, str)
        self.assertIsInstance(self.state.created_at, datetime.datetime)
        self.assertIsInstance(self.state.updated_at, datetime.datetime)
        self.assertIsInstance(self.state.id, str)

    def assertHasAttr(self, obj, attr):
        self.assertTrue(hasattr(obj, attr), f"{obj} has no attribute {attr}")


if __name__ == "__main__":
    unittest.main()
