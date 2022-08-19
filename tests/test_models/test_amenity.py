"""test_amenity Module."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Defines tests for the methods in Amenity."""

    def setUp(self):
        """Create some Amenity objects for testing purposes."""
        self.a1 = Amenity()

    def test_init(self):
        """Test that a new object is initialized correctly."""
        # check Amenity is subclass of BaseModel
        self.assertTrue(issubclass(Amenity, BaseModel))

        self.assertIsInstance(self.a1, Amenity)

        # test that a newly created object has the correct attributes
        attrs = {
            "name": str
        }

        for a_name, a_type in attrs.items():
            self.assertTrue(hasattr(self.a1, a_name))
            self.assertIsInstance(getattr(self.a1, a_name, None), a_type)
