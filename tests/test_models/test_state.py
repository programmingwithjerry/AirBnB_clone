#!/usr/bin/python3
"""
Unit tests for the State class.
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test suite for the State class.
    """

    def test_instance_creation(self):
        """
        Verify that a State instance can be created.
        """
        state_instance = State()
        self.assertTrue(isinstance(state_instance, State))

