#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def test_all_method(self):
        """
        Test the all() method of FileStorage.
        """
        storage = FileStorage()
        objects = storage.all()
        for key, value in objects.items():
            self.assertTrue(issubclass(eval(key.split('.')[0]), BaseModel))

