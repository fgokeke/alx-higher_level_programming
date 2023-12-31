#!/usr/bin/python3
"""Test cases for the Square class"""
import unittest
from models.square import Square
import sys
from io import StringIO


class TestSquare(unittest.TestCase):
    """Defines various test cases for the Square class"""

    def test_constructor_valid_args(self):
        """
        Test the constructor with valid arguments.
        """
        s = Square(5, 2, 3, 42)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 42)

    def test_constructor_default_args(self):
        """
        Test the constructor with default arguments.
        """
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_constructor_invalid_size_type(self):
        """
        Test the constructor with an invalid type for size.
        """
        with self.assertRaises(ValueError):
            s = Square(-5)

    def test_constructor_invalid_x_type(self):
        """
        Test the constructor with an invalid type for x.
        """
        with self.assertRaises(TypeError):
            s = Square(5, "invalid")

    def test_constructor_negative_x(self):
        """
        Test the constructor with a negative x-coordinate.
        """
        with self.assertRaises(ValueError):
            s = Square(5, -2)

    def test_constructor_invalid_y_type(self):
        """
        Test the constructor with an invalid type for y.
        """
        with self.assertRaises(TypeError):
            s = Square(5, 2, "invalid")

    def test_constructor_negative_y(self):
        """
        Test the constructor with a negative y-coordinate.
        """
        with self.assertRaises(ValueError):
            s = Square(5, 2, -3)

    def test_area(self):
        """
        Test the area of the square.
        """
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

        s2 = Square(10)
        self.assertEqual(s2.area(), 100)

        s3 = Square(8, 2, 1)
        self.assertEqual(s3.area(), 64)

        with self.assertRaises(ValueError):
            s4 = Square(0)
            s4.area()

    def test_display(self):
        """
        Test the display method for the square.
        """
        s = Square(4)
        expected_output = "####\n####\n####\n####\n"
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            s.display()
            output = out.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            sys.stdout = saved_stdout

    def test_str(self):
        """
        Test the string representation of the square.
        """
        s = Square(5, 2, 3, 42)
        self.assertEqual(str(s), "[Square] (42) 2/3 - 5")

    def test_update_args(self):
        """
        Test the update method with *args.
        """
        s = Square(5, 2, 3, 42)
        s.update(89, 10, 4, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.id, 89)

    def test_update_kwargs(self):
        """
        Test the update method with **kwargs.
        """
        s = Square(5, 2, 3, 42)
        s.update(id=89, x=4, size=10, y=1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.id, 89)

    def test_update_args_kwargs_combined(self):
        """
        Test the update method with a combination of *args and **kwargs.
        """
        s = Square(5, 2, 3, 42)
        s.update(89, 10, 4, x=1, size=15)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 89)

    def test_update_empty_args(self):
        """
        Test the update method with empty *args.
        """
        s = Square(5, 2, 3, 42)
        s.update()
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 42)

    def test_update_invalid_args(self):
        """
        Test the update method with invalid values as *args.
        """
        s = Square(5, 2, 3, 42)
        with self.assertRaises(TypeError):
            s.update(89, "invalid", 3.5, 4)

        with self.assertRaises(ValueError):
            s.update(89, -2, 3, 4)

    def test_update_invalid_kwargs(self):
        """
        Test the update method with invalid values as **kwargs.
        """
        s = Square(5, 2, 3, 42)
        with self.assertRaises(ValueError):
            s.update(id=89, x=-2, size=3, y=4)

        with self.assertRaises(TypeError):
            s.update(id=89, x="2", size=3.5, y=4)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method for the Square.
        """
        s = Square(5, 2, 3, 42)
        square_dict = s.to_dictionary()
        expected_dict = {
            'id': 42,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(square_dict, expected_dict)

    def test_to_dictionary_default(self):
        """
        Test the to_dictionary method for a Square with default values.
        """
        s = Square(5)
        square_dict = s.to_dictionary()
        expected_dict = {
            'id': s.id,
            'size': 5,
            'x': 0,
            'y': 0
        }
        self.assertEqual(square_dict, expected_dict)

    def test_to_dictionary_no_id(self):
        """
        Test the to_dictionary method for a Square with no specified ID.
        """
        s = Square(5, 2, 3)
        square_dict = s.to_dictionary()
        expected_dict = {
            'id': s.id,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(square_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
