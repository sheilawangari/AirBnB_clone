"""test_file_storage Module."""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Defines tests for the methods in FileStorage."""

    def setUp(self):
        """Create some FileStorage objects for testing purposes."""
        self.fs = FileStorage()

    def tearDown(self):
        """Clear all objects in __objects."""
        FileStorage._FileStorage__objects.clear()

    def test_init(self):
        """Test that object attributes are initialized correctly."""
        # test that objects are instances of the class
        self.assertIsInstance(self.fs, FileStorage)

        # test that __file_path is valid
        fp = FileStorage._FileStorage__file_path
        self.assertTrue(type(fp) is str and len(fp) > 0)

        # test that __objects is valid
        fs_obj = FileStorage._FileStorage__objects
        self.assertTrue(type(fs_obj) is dict)

    def test_get_cls(self):
        """Test the get_cls method of FileStorage."""
        from models.base_model import BaseModel

        self.assertIs(self.fs.get_cls("BaseModel"), BaseModel)
        self.assertIsNone(self.fs.get_cls("Model"))

    def test_all(self):
        """Test the all method of FileStorage."""
        fs_obj = FileStorage._FileStorage__objects
        self.assertIs(self.fs.all(), fs_obj)

    def test_new(self):
        """Test the new method of FileStorage."""
        from models.base_model import BaseModel

        fs_obj = FileStorage._FileStorage__objects

        # create new object
        obj = BaseModel()
        obj_id = type(obj).__name__ + "." + str(obj.id)

        # check that the new object is now in __objects
        self.assertEqual(fs_obj.get(obj_id), obj)

    def test_delete(self):
        """Test the delete method of FileStorage."""
        from models.base_model import BaseModel

        fs_obj = FileStorage._FileStorage__objects

        # create new object
        obj = BaseModel()
        obj_id = type(obj).__name__ + "." + str(obj.id)

        # check that the new object is now in __objects
        self.assertEqual(fs_obj.get(obj_id), obj)

        # delete the object
        self.fs.delete(obj_id)

        # check that the new object is now not in __objects
        self.assertEqual(fs_obj.get(obj_id), None)

    def test_save(self):
        """Test the save method of FileStorage."""
        import os

        fp = FileStorage._FileStorage__file_path

        # remove the json file
        try:
            os.remove(fp)
        except Exception:
            pass

        self.assertFalse(os.path.exists(fp))

        # saving should create a new file
        self.fs.save()
        self.assertTrue(os.path.exists(fp))

        try:
            os.remove(fp)
        except Exception:
            pass

    def test_reload(self):
        """Test the reload method of FileStorage."""
        import os
        from models.base_model import BaseModel

        fp = FileStorage._FileStorage__file_path
        fs_obj = FileStorage._FileStorage__objects

        # remove the json file
        try:
            os.remove(fp)
        except Exception:
            pass

        # create some new BaseModel objects and save to the json file
        for i in range(2):
            BaseModel()

        fs_obj_copy = dict(fs_obj)
        self.fs.save()

        # clear the __objects dictionary and ensure that it is empty
        fs_obj.clear()
        self.assertTrue(len(fs_obj) == 0)

        # reload __objects from json file
        self.fs.reload()

        # check that __objects has the same items as before deletion
        self.assertEqual(fs_obj.keys(), fs_obj_copy.keys())

        try:
            os.remove(fp)
        except Exception:
            pass
