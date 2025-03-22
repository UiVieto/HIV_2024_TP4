import os
import sys

sys.path.append(os.getcwd())
sys.path.append('..')

from poly_llm.to_test.find_closest_elements import find_closest_elements

# Début d'ouput du LLM
import unittest
from typing import List, Tuple

class TestFindClosestElementsFunction(unittest.TestCase):

    def test_find_closest_elements_distinct(self):
        # Test with distinct closest elements
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([10.0, 20.0, 30.0, 40.0, 50.0, 20.5]), (20.0, 20.5))

    def test_find_closest_elements_equal(self):
        # Test with equal closest elements
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))
        self.assertEqual(find_closest_elements([10.0, 20.0, 30.0, 40.0, 50.0, 20.0]), (20.0, 20.0))

    def test_find_closest_elements_negative(self):
        # Test with negative numbers
        self.assertEqual(find_closest_elements([-1.0, -2.0, -3.0, -4.0, -5.0, -2.2]), (-2.2, -2.0))
        self.assertEqual(find_closest_elements([-10.0, -20.0, -30.0, -40.0, -50.0, -20.5]), (-20.5, -20.0))

    def test_find_closest_elements_mixed(self):
        # Test with mixed positive and negative numbers
        self.assertEqual(find_closest_elements([-1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([-10.0, 20.0, 30.0, 40.0, 50.0, 20.5]), (20.0, 20.5))

    def test_find_closest_elements_duplicates(self):
        # Test with duplicate numbers
        self.assertEqual(find_closest_elements([1.0, 1.0, 1.0, 2.0, 3.0]), (1.0, 1.0))
        self.assertEqual(find_closest_elements([10.0, 10.0, 10.0, 20.0, 30.0]), (10.0, 10.0))

    def test_find_closest_elements_at_least_two(self):
        # Test with list of length at least two
        with self.assertRaises(ValueError):
            find_closest_elements([1.0])

if __name__ == '__main__':
    unittest.main()
