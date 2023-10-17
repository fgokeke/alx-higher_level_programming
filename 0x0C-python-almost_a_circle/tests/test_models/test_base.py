#!/usr/bin/python3
"""Test cases for the Base Model"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import json
import os


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
    def setUp(self):
        """Clear any existing JSON files before running the tests"""
        for filename in ["Rectangle.json", "Square.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def tearDown(self):
        """Clear any JSON files created during the tests"""
        for filename in ["Rectangle.json", "Square.json"]:
            if os.path.exists(filename):
                os.remove(filename)

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

    def test_to_json_string(self):
        """
        Test the to_json_string method.
        """
        list_of_dicts = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        json_string = Base.to_json_string(list_of_dicts)
        self.assertEqual(json.loads(json_string), list_of_dicts)

        empty_list = []
        empty_json_string = Base.to_json_string(empty_list)
        self.assertEqual(empty_json_string, "[]")

        none_json_string = Base.to_json_string(None)
        self.assertEqual(none_json_string, "[]")

    def test_from_json_string(self):
        """Test from_json_string method"""
        r1 = Rectangle(10, 20, 1, 2)
        r2 = Rectangle(5, 5, 3, 4)
        r_dict1 = r1.to_dictionary()
        r_dict2 = r2.to_dictionary()
        json_str = Base.to_json_string([r_dict1, r_dict2])
        obj_list = Base.from_json_string(json_str)
        self.assertEqual(obj_list, [r_dict1, r_dict2])

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(10, 20, 1, 2)
        r2 = Rectangle(5, 5, 3, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_with_square(self):
        """Test save_to_file method with Square class"""
        s1 = Square(10, 1, 2)
        s2 = Square(5, 3, 4)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_empty(self):
        """Test save_to_file method with an empty list"""
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_none(self):
        """Test save_to_file method with None as input"""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))


if __name__ == '__main__':
    unittest.main()
