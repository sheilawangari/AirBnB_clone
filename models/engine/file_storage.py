#!/usr/bin/python3
"""file_storage module."""
import json


class FileStorage:
    """Serializes and deserializes JSON."""

    __file_path = "file.json"
    __objects = {}

    def get_cls(self, name):
        """Return a dict of all valid classes and their constructors."""
        from models.base_model import BaseModel
        from models.user import User

        classes = {
            "BaseModel": BaseModel,
            "User": User
        }

        return classes.get(name)

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        cls_name = type(obj).__name__
        key = cls_name + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def delete(self, id):
        """Delete object with the given id from __objects."""
        try:
            FileStorage.__objects.pop(id)
        except Exception:
            pass

    def update(self, obj_id, attr_name, attr_value):
        """Update given attribute of given object with given value."""
        # get corresponding object
        obj = FileStorage.__objects.get(obj_id)
        attr_type = type(getattr(obj, attr_name, ""))

        # set attribute in given object
        try:
            setattr(obj, attr_name, attr_type(attr_value))
        except Exception:
            print(f"Unable to set {attr_name} to {attr_value}")

    def save(self):
        """Serialize __objects to the JSON file."""
        # create object to serialize
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
        path = FileStorage.__file_path
        my_dict = {}

        try:
            with open(path, "r", encoding="utf-8") as f_read:
                my_dict = json.load(f_read)
        except Exception:
            pass

        for key, value in my_dict.items():
            cls_name = key.split('.')[0]
            cls = self.get_cls(cls_name)

            FileStorage.__objects[key] = cls(**value)
