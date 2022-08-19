"""test_state Module."""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Defines tests for the methods in State."""

    def setUp(self):
        """Create some State objects for testing purposes."""
        self.s1 = State()

    def test_init(self):
        """Test that a new object is initialized correctly."""
        # check State is subclass of BaseModel
        self.assertTrue(issubclass(State, BaseModel))

        self.assertIsInstance(self.s1, State)

        # test that a newly created object has the correct attributes
        attrs = {
            "name": str
        }

        for a_name, a_type in attrs.items():
            self.assertTrue(hasattr(self.s1, a_name))
            self.assertIsInstance(getattr(self.s1, a_name, None), a_type)
