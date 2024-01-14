#! usr/bin/python3


"""

A test module for the rectangle class

"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_init(unittest.TestCase):

    def test_is_a_child(self):
        self.assertIsInstance(Rectangle(5, 6), Base)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_two_args(self):
        r1 = Rectangle(2, 4)
        r2 = Rectangle(5, 6)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(5, 6, 7)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, 20).id, 20)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 4, 3, 5, 6).__width

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 4, 3, 5, 6).__height

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 4, 3, 5, 6).__x

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 4, 3, 5, 6).__y

    def test_width_getter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(r1.width, 2)

    def test_width_setter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r1.width = 6
        self.assertEqual(r1.width, 6)

    def test_height_getter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(r1.height, 4)

    def test_width_setter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r1.height = 6
        self.assertEqual(r1.height, 6)

    def test_x_getter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(r1.x, 6)

    def test_x_setter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r1.x = 5
        self.assertEqual(r1.x, 5)

    def test_y_getter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(r1.y, 8)

    def test_y_setter(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r1.y = 6
        self.assertEqual(r1.y, 6)
