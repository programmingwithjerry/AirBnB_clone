#!/usr/bin/python3
"""
Defines the User class.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place.

    Attributes:
    city_id: string - the ID of the city, initially an empty string.
    user_id: string - the ID of the user, initially an empty string.
    name: string - the name of the place.
    description: string - a description of the place.
    number_rooms: integer - the number of rooms in the place.
    number_bathrooms: integer - the number of bathrooms in the place.
    max_guest: integer - the maximum guest capacity of the place.
    price_by_night: integer - the price per night for the place.
    latitude: float - the latitude of the place.
    longitude: float - the longitude of the place.
    amenity_ids: list of string - a list of Amenity IDs, initially an empty list.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

