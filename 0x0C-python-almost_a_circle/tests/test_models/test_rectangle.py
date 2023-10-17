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

    def test_update(self):
        """
        Test the update method of the Rectangle class.
        """
        r = Rectangle(5, 8, 2, 3, 42)

        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 2/3 - 5/8")

        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 2/3 - 2/8")

        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 2/3 - 2/3")

        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/3 - 2/3")

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_invalid_types(self):
        """
        Test the update method with invalid argument types.
        """
        r = Rectangle(5, 8, 2, 3, 42)

        with self.assertRaises(TypeError):
            r.update(89, "2")

        with self.assertRaises(TypeError):
            r.update(89, 2, "3")

    def test_update_more_than_5_args(self):
        """
        Test the update method with more than 5 arguments.
        """
        r = Rectangle(5, 8, 2, 3, 42)

        r.update(89, 2, 3, 4, 5, 6, 7, 8)

        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_invalid_args(self):
        """
        Test the update method with invalid values as arguments.
        """
        r = Rectangle(5, 8, 2, 3, 42)
        with self.assertRaises(ValueError):
            r.update("invalid", -2, 3.5, 4, -5)

    def test_update_empty(self):
        """
        Test the update method with no arguments.
        """
        r = Rectangle(5, 8, 2, 3, 42)
        r.update()

        self.assertEqual(str(r), "[Rectangle] (42) 2/3 - 5/8")

        self.assertEqual(r.id, 42)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_update_with_kwargs(self):
        """
        Test the update method with keyword arguments (kwargs).
        """
        r = Rectangle(5, 8, 2, 3, 42)
        r.update(height=1, width=2, x=3, y=5, id=89)

        self.assertEqual(str(r), "[Rectangle] (89) 3/5 - 2/1")

    def test_update_with_mixed_args_kwargs(self):
        """
        Test the update method with a mix of positional and keyword arguments.
        """
        r = Rectangle(5, 8, 2, 3, 42)
        r.update(89, width=2, x=3, height=1)

        self.assertEqual(str(r), "[Rectangle] (89) 2/3 - 5/8")

    def test_update_invalid_kwargs(self):
        """
        Test the update method with invalid attribute names in
        keyword arguments.
        """
        r = Rectangle(5, 8, 2, 3, 42)

        r.update(invalid_attr=1, invalid_attr2=2)

        self.assertEqual(str(r), "[Rectangle] (42) 2/3 - 5/8")

    def test_to_dictionary(self):
        """
        Test the to_dictionary method for the Rectangle.
        """
        r = Rectangle(5, 8, 2, 3, 42)
        rect_dict = r.to_dictionary()
        expected_dict = {
            'id': 42,
            'width': 5,
            'height': 8,
            'x': 2,
            'y': 3
        }
        self.assertEqual(rect_dict, expected_dict)

    def test_to_dictionary_default(self):
        """
        Test the to_dictionary method for the Rectangle with default values.
        """
        r = Rectangle(5, 8)
        rect_dict = r.to_dictionary()
        expected_dict = {
            'id': r.id,
            'width': 5,
            'height': 8,
            'x': 0,
            'y': 0
        }
        self.assertEqual(rect_dict, expected_dict)

    def test_to_dictionary_change_attributes(self):
        """
        Test the to_dictionary method after changing attributes.
        """
        r = Rectangle(5, 8, 2, 3, 42)
        r.width = 10
        r.height = 12
        r.x = 7
        r.y = 9
        rect_dict = r.to_dictionary()
        expected_dict = {
            'id': 42,
            'width': 10,
            'height': 12,
            'x': 7,
            'y': 9
        }
        self.assertEqual(rect_dict, expected_dict)

    def test_to_dictionary_after_update(self):
        """
        Test the to_dictionary method after using the update method.
        """
        r = Rectangle(5, 8, 2, 3, 42)
        r.update(89, 10, 12, 7, 9)
        rect_dict = r.to_dictionary()
        expected_dict = {
            'id': 89,
            'width': 10,
            'height': 12,
            'x': 7,
            'y': 9
        }
        self.assertEqual(rect_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
