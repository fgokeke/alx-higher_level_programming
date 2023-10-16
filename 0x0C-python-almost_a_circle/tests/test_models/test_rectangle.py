#!/usr/bin/python3
"""Test cases for the Rectangle class"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    def test_constructor_valid_args(self):
        """
        Test the constructor with valid arguments.
        """
        r = Rectangle(5, 8, 2, 3, 42)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 42)

    def test_constructor_default_args(self):
        """
        Test the constructor with default arguments.
        """
        r = Rectangle(5, 8)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_constructor_invalid_width_type(self):
        """
        Test the constructor with an invalid type for width.
        """
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 8)

    def test_constructor_invalid_height_type(self):
        """
        Test the constructor with an invalid type for height.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(5, "invalid")

    def test_constructor_negative_width(self):
        """
        Test the constructor with a zero or negative width.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 8)

    def test_constructor_negative_height(self):
        """
        Test the constructor with a zero or negative height.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(5, -8)

    def test_constructor_invalid_x_type(self):
        """
        Test the constructor with an invalid type for x.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(5, 8, "invalid")

    def test_constructor_negative_x(self):
        """
        Test the constructor with a negative x-coordinate.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(5, 8, -2)

    def test_constructor_invalid_y_type(self):
        """
        Test the constructor with an invalid type for y.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(5, 8, 2, "invalid")

    def test_constructor_negative_y(self):
        """
        Test the constructor with a negative y-coordinate.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(5, 8, 2, -3)

    def test_area(self):
        """
        Test the area of the rectangle
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

        with self.assertRaises(ValueError):
            r4 = Rectangle(0, 5)
            r4.area()

        r5 = Rectangle(10**6, 10**6)
        self.assertEqual(r5.area(), 10**12)

        with self.assertRaises(ValueError):
            r6 = Rectangle(-5, 5)
            r6.area()

        with self.assertRaises(TypeError):
            r7 = Rectangle(2.5, 5)
            r7.area()

    def test_display(self):
        """
        Test the display method of the Rectangle class.
        """
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            r.display()
            output = out.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            sys.stdout = saved_stdout

    def test_display_x_offset(self):
        """
        Test the display method with an x offset.
        """
        r = Rectangle(3, 2, 2)
        expected_output = "  ###\n  ###\n"

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            r.display()
            output = out.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            sys.stdout = saved_stdout

    def test_display_y_offset(self):
        """
        Test the display method with a y offset.
        """
        r = Rectangle(3, 2, 0, 2)
        expected_output = "\n\n###\n###\n"

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            r.display()
            output = out.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            sys.stdout = saved_stdout

    def test_display_x_and_y_offset(self):
        """
        Test the display method with both x and y offsets.
        """
        r = Rectangle(4, 3, 2, 1)
        expected_output = "\n  ####\n  ####\n  ####\n"

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            r.display()
            output = out.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            sys.stdout = saved_stdout

    def test_str(self):
        """
        Test the __str__ method of the Rectangle class.
        """
        r = Rectangle(5, 8, 2, 3, 42)
        expected_str = "[Rectangle] (42) 2/3 - 5/8"
        self.assertEqual(str(r), expected_str)


if __name__ == '__main__':
    unittest.main()
