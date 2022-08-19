"""test_place Module."""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Defines tests for the methods in Place."""

    def setUp(self):
        """Create some Place objects for testing purposes."""
        self.p1 = Place()

    def test_init(self):
        """Test that a new object is initialized correctly."""
        # check Place is subclass of BaseModel
        self.assertTrue(issubclass(Place, BaseModel))

        self.assertIsInstance(self.p1, Place)

        # test that a newly created object has the correct attributes
        attrs = {
            "city_id": str,
            "user_id": str,
            "name": str,
            "description": str,
            "number_rooms": int,
            "number_bathrooms": int,
            "max_guest": int,
            "price_by_night": int,
            "latitude": float,
            "longitude": float,
            "amenity_ids": list
        }

        for a_name, a_type in attrs.items():
            self.assertTrue(hasattr(self.p1, a_name))
            self.assertIsInstance(getattr(self.p1, a_name, None), a_type)
