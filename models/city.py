#!/usr/bin/python3
"""
Defines the User class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city.

    Attributes:
    name: The name of the city.
    state_id: The ID of the state.
    """
    name = ""
    state_id = ""

