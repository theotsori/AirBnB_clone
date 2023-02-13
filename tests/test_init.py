#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):

    def test_new(self):
        storage = FileStorage("file.json")
        state = State()
        state.name = "California"
        storage.new(state)
        self.assertIn(state, storage.all().values())

    def test_reload(self):
        storage = FileStorage("file.json")
        state = State()
        state.name = "California"
        storage.new(state)
        storage.save()
        storage.reload()
        #  self.assertIn(state, storage.all().values())

    def test_save(self):
        storage = FileStorage("file.json")
        state = State()
        state.name = "California"
        storage.new(state)
        storage.save()
        storage_all = storage.all()
        state_key = state.__class__.__name__ + "." + state.id
        self.assertIn(state_key, storage_all.keys())


if __name__ == '__main__':
    unittest.main()
