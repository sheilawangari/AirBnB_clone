#!/usr/bin/python3
"""base_model module."""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """Initialise attributes of BaseModel object."""
        # assign with an uuid when an instance is created
        self.id = str(uuid.uuid4())
        # assign with the current datetime when an instance is created
        self.created_at = datetime.now()
        # assign with the current datetime when an instance is created/updated
        self.updated_at = self.created_at

    def __str__(self):
        """Return string representation of BaseModel object."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the public instance attribute updated_at."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance."""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict
