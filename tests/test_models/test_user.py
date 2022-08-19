"""test_user Module."""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Defines tests for the methods in User."""

    def setUp(self):
        """Create some User objects for testing purposes."""
        self.u1 = User()

    def test_init(self):
        """Test that a new object is initialized correctly."""
        # check User is subclass of BaseModel
        self.assertTrue(issubclass(User, BaseModel))

        self.assertIsInstance(self.u1, User)

        # test that a newly created object has the correct attributes
        attrs = {
            "email": str,
            "password": str,
            "first_name": str,
            "last_name": str
        }

        for a_name, a_type in attrs.items():
            self.assertTrue(hasattr(self.u1, a_name))
            self.assertIsInstance(getattr(self.u1, a_name, None), a_type)
