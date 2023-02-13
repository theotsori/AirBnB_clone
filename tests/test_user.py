#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_instance(self):
        """Tests if the object is an instance of BaseModel and User"""
        self.assertIsInstance(self.user, BaseModel)
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Tests if the object has the correct attributes"""
        self.assertHasAttr(self.user, "email")
        self.assertHasAttr(self.user, "password")
        self.assertHasAttr(self.user, "first_name")
        self.assertHasAttr(self.user, "last_name")

    def test_type(self):
        """Tests if the type of the attributes is correct"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def assertHasAttr(self, obj, attr):
        """Helper function to test if an object has an attribute"""
        self.assertTrue(hasattr(obj, attr))


if __name__ == "__main__":
    unittest.main()
