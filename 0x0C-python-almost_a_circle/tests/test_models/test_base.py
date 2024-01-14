#! usr/bin/python3


"""

A test module for the class Base

"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b3.id - 1)

    def test_unique_id(self):
        self.assertEqual(Base(12).id, 12)

    def test_nb_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_nb_after_del(self):
        b1 = Base()
        old_nb = Base().id
        del b1
        b2 = Base()
        self.assertEqual(old_nb, b2.id - 1)

    def test_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_str_id(self):
        self.assertEqual(Base("hi").id, "hi")

    def test_bytes_id(self):
        self.assertEqual(Base(b"hi").id, b"hi")

    def test_bytearray_id(self):
        self.assertEqual(Base(bytearray(b"hi")).id, bytearray(b"hi"))

    def test_memoryview_id(self):
        self.assertEqual(Base(memoryview(b"hi")).id, memoryview(b"hi"))

    def test_list_id(self):
        self.assertEqual(Base([1, 2]).id, [1, 2])

    def test_tuple_id(self):
        self.assertEqual(Base((2, 5)).id, (2, 5))

    def test_dict_id(self):
        self.assertEqual(Base({"hol": "sch"}).id, {"hol": "sch"})

    def test_negative_id(self):
        self.assertEqual(Base(-5).id, -5)

    def test_float_id(self):
        self.assertEqual(Base(5.6).id, 5.6)

    def test_NaN_id(self):
        self.assertNotEqual(Base(float('nan')).id, float('nan'))

    def test_inf_id(self):
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_complex_id(self):
        self.assertEqual(Base(complex(5)).id, complex(5))

    def test_bool_id(self):
        self.assertEqual(Base(True).id, True)

    def test_set_id(self):
        self.assertEqual(Base({5, 6}).id, {5, 6})

    def test_frozen_set_id(self):
        self.assertEqual(Base(frozenset({5, 6})).id, frozenset({5, 6}))

    def test_range_id(self):
        self.assertEqual(Base(range(5)).id, range(5))

    def test_public_attribute(self):
        b1 = Base(20)
        b1.id = 25
        self.assertEqual(b1.id, 25)

    def test_private_attribute(self):
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects())

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Base(2, 5)
