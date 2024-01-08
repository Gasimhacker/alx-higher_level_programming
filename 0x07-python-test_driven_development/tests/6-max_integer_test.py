#!/usr/bin/python3

"""Unittests module for max_integer([])"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInt(unittest.TestCase):
    """Define unittests for the max_integer([])"""

    def test_integers(self):
        """ Test integers only """
        self.assertEqual(max_integer([1, 5, 66, -10]), 66)

    def test_ints_floats(self):
        """ Test integers combined with floats"""
        self.assertEqual(max_integer([1, 5, 6.66, -10]), 6.66)
        self.assertEqual(max_integer([1, 66.0, 66, -10]), 66)

    def test_strings(self):
        """Test a string"""
        self.assertEqual(max_integer("hello"), "o")

    def test_tuples(self):
        """ Test a tuple"""
        self.assertEqual(max_integer((5, 6)), 6)

    def test_list_of_strings(self):
        """ Test a list of strings"""
        self.assertEqual(max_integer(["h", "e", "l", "o"]), "o")
        self.assertEqual(max_integer(["abb", "abc"]), "abc")

    def test_list_of_tuples(self):
        """ Test a list of tuples"""
        self.assertEqual(max_integer([(1, 5), (1, 66)]), (1, 66))

    def test_empty(self):
        """ Test an empty list"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)
