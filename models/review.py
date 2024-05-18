#!/usr/bin/python3
"""
Defines the User class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review.

    Attributes:
    place_id: string - the ID of the place, initially an empty string.
    user_id: string - the ID of the user, initially an empty string.
    text: string - the review text, which can be an empty string.
    """
    place_id = ""
    user_id = ""
    text = ""

