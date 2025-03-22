import os
import sys

sys.path.append(os.getcwd())
sys.path.append('..')

from poly_llm.to_test.closest_integer import closest_integer

# Début de l'ouput du LLM
import unittest

class TestClosestIntegerFunction(unittest.TestCase):

    def test_closest_integer_positive(self):
        # Test with positive numbers
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("14.4"), 14)
        self.assertEqual(closest_integer("14.6"), 15)
        self.assertEqual(closest_integer("14"), 14)

    def test_closest_integer_negative(self):
        # Test with negative numbers
        self.assertEqual(closest_integer("-14.5"), -15)
        self.assertEqual(closest_integer("-14.4"), -14)
        self.assertEqual(closest_integer("-14.6"), -15)
        self.assertEqual(closest_integer("-14"), -14)

    def test_closest_integer_zero(self):
        # Test with zero
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("-0.5"), -1)

    def test_closest_integer_decimal(self):
        # Test with decimal numbers
        self.assertEqual(closest_integer("14.123"), 14)
        self.assertEqual(closest_integer("14.567"), 15)
        self.assertEqual(closest_integer("-14.123"), -14)
        self.assertEqual(closest_integer("-14.567"), -15)

    def test_closest_integer_empty_string(self):
        # Test with empty string
        self.assertEqual(closest_integer(""), 0)

    def test_closest_integer_trailing_zeros(self):
        # Test with trailing zeros
        self.assertEqual(closest_integer("14.500"), 15)
        self.assertEqual(closest_integer("14.400"), 14)
        self.assertEqual(closest_integer("-14.500"), -15)
        self.assertEqual(closest_integer("-14.400"), -14)

if __name__ == '__main__':
    unittest.main()
