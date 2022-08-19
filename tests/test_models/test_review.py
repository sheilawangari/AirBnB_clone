"""test_review Module."""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Defines tests for the methods in Review."""

    def setUp(self):
        """Create some Review objects for testing purposes."""
        self.r1 = Review()

    def test_init(self):
        """Test that a new object is initialized correctly."""
        # check Review is subclass of BaseModel
        self.assertTrue(issubclass(Review, BaseModel))

        self.assertIsInstance(self.r1, Review)

        # test that a newly created object has the correct attributes
        attrs = {
            "place_id": str,
            "user_id": str,
            "text": str
        }

        for a_name, a_type in attrs.items():
            self.assertTrue(hasattr(self.r1, a_name))
            self.assertIsInstance(getattr(self.r1, a_name, None), a_type)
