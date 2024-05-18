#!/usr/bin/python3
"""
The BaseModel class provides shared attributes and methods for other classes.
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """Represents the base model with common attributes and methods.

    Attributes:
    id: A unique identifier for each instance.
    created_at: The timestamp when the instance was created.
    updated_at: The timestamp when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """Initializes BaseModel with id, created_at, and updated_at attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current datetime and saves the instance."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance, including formatted datetime attributes."""
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict

