#!/usr/bin/python3
"""
Unit tests for the City class.
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class CityTestCase(unittest.TestCase):
    """
    Test suite for the City class.
    """

    def test_instance_creation(self):
        """
        Test creating an instance of City.
        """
        city_instance = City()
        self.assertTrue(isinstance(city_instance, City))

