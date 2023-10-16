#!/usr/bin/python3
"""Test cases for the Base Model"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Unit tests for the Base class.

    The Base class is responsible for managing
    unique identifiers in the project. This test suite
    checks the correct behavior of the Base class,
    including the auto-incrementing of 'id' and the
    assignment of a specific 'id'.

    Attributes:
        None

    Methods:
        test_auto_increment_id: Test the auto-increment behavior of 'id'.
        test_specific_id: Test the assignment of a specific 'id'.
    """
    def test_auto_increment_id(self):
        """
        Test auto-incrementing 'id' attribute.
        """
        instance1 = Base()
        instance2 = Base()
        instance3 = Base()

        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertEqual(instance1.id + 1, instance2.id)
        self.assertEqual(instance3.id, 3)

    def test_specific_id(self):
        """
        Test the assignment of a specific 'id'.
        """
        instance1 = Base(42)
        instance2 = Base(-5)
        instance3 = Base(0)
        instance4 = Base(1000000)
        instance5 = Base(10)
        instance5.id = 43

        self.assertEqual(instance1.id, 42)
        self.assertEqual(instance2.id, -5)
        self.assertEqual(instance3.id, 0)
        self.assertEqual(instance4.id, 1000000)
        self.assertEqual(instance5.id, 43)

    def test_private_attribute_access(self):
        """
        Testing the Privacy of the '__nb_objects' Attribute
        """
        instance = Base()
        with self.assertRaises(AttributeError):
            count = instance.__nb_objects


if __name__ == '__main__':
    unittest.main()
