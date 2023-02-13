#!/usr/bin/python3

import os
import unittest
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Setting up the test environment"""
        self.storage = FileStorage("file.json")

    def test_all(self):
        """Test if the 'all' method returns the right object"""
        state = State()
        state.name = "California"
        self.storage.new(state)
        self.assertIn(state, self.storage.all().values())

    def test_new(self):
        """Test if the 'new' method works correctly"""
        state = State()
        state.name = "California"
        self.storage.new(state)
        all_objects = self.storage.all()
        key = "{}.{}".format(state.__class__.__name__, state.id)
        self.assertIn(key, all_objects.keys())

    def test_save_reload(self):
        """Test if the 'save' and 'reload' methods work correctly"""
        state = State()
        state.name = "California"
        self.storage.new(state)
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        key = "{}.{}".format(state.__class__.__name__, state.id)
        self.assertIn(key, all_objects.keys())


if __name__ == '__main__':
    unittest.main()
