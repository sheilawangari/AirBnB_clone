#!/usr/bin/python3
"""file_storage module."""
import json


class FileStorage:
    """Serializes and deserializes JSON."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        class_name = type(obj).__name__
        key = class_name + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        # creat object to serialize
        path = FileStorage.__file_path
        my_dict = {}

        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        try:
            with open(path, "w", encoding="utf-8") as f_write:
                json.dump(my_dict, f_write)
        except Exception:
            pass

    def reload(self):
        """Deserializes the JSON file to __objects."""
        from models.base_model import BaseModel

        path = FileStorage.__file_path
        my_dict = {}

        try:
            with open(path, "r", encoding="utf-8") as f_read:
                my_dict = json.load(f_read)
        except Exception:
            pass

        for key, value in my_dict.items():
            FileStorage.__objects[key] = BaseModel(**value)
