#!/usr/bin/python3

import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from entry_point import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb = HBNBCommand()
        self.base_model = BaseModel()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()

    def test_quit_command(self):
        self.assertTrue(self.hbnb.do_quit(""))

    def test_EOF_command(self):
        self.assertTrue(self.hbnb.do_EOF(""))

    def test_emptyline_command(self):
        self.assertIsNone(self.hbnb.emptyline())
