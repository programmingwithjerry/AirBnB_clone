#!/usr/bin/python3
"""This module contains all test cases for the BaseModel class."""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Defines the test cases for the BaseModel class."""

    def setUp(self):
        """Initialize instances before each test."""
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def test_uuid(self):
        """Test UUID generation and uniqueness."""
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertIsInstance(self.bm1.id, str)
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_instance_type(self):
        """Test the type of the instance."""
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertIsInstance(str(self.bm1), str)
        self.assertEqual(str(self.bm2),
                         "[BaseModel] ({}) {}".format(self.bm2.id, self.bm2.__dict__))

    def test_to_dict(self):
        """Test the dictionary representation of an instance."""
        self.assertIsInstance(self.bm2.to_dict(), dict)

    def test_type_created_at(self):
        """Test if the type of created_at attribute is datetime."""
        self.assertIsInstance(self.bm1.created_at, datetime)

    def test_type_updated_at(self):
        """Test if the type of updated_at attribute is datetime."""
        self.assertIsInstance(self.bm1.updated_at, datetime)

