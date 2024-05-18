#!/usr/bin/python3
"""
Defines the User class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity.

    Attributes:
    name: The name of the amenity.
    """
    name = ""

