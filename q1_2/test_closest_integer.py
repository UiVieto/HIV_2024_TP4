import os
import sys

sys.path.append(os.getcwd())
sys.path.append('..')

from poly_llm.to_test.closest_integer import closest_integer

# Début de l'ouput du LLM
import unittest

class TestClosestInteger(unittest.TestCase):
    def test_exact_integer(self):
        self.assertEqual(closest_integer("10"), 10)

    def test_half_away_from_zero_positive(self):
        self.assertEqual(closest_integer("14.5"), 15)

    def test_half_away_from_zero_negative(self):
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_half_towards_zero_positive(self):
        self.assertEqual(closest_integer("14.4"), 14)

    def test_half_towards_zero_negative(self):
        self.assertEqual(closest_integer("-14.4"), -14)

    def test_decimal_towards_zero(self):
        self.assertEqual(closest_integer("10.2"), 10)

    def test_decimal_away_from_zero(self):
        self.assertEqual(closest_integer("10.7"), 11)

    def test_zero(self):
        self.assertEqual(closest_integer("0"), 0)

    def test_zero_point_five(self):
        self.assertEqual(closest_integer("0.5"), 1)

    def test_negative_zero_point_five(self):
        self.assertEqual(closest_integer("-0.5"), -1)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            closest_integer("")

    def test_non_numeric_string(self):
        with self.assertRaises(ValueError):
            closest_integer("abc")

if __name__ == '__main__':
    unittest.main()