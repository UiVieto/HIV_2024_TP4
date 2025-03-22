import os
import sys

sys.path.append(os.getcwd())
sys.path.append('..')

from poly_llm.to_test.find_closest_elements import find_closest_elements

# Début de l'output du LLM
import unittest
from typing import List, Tuple

class TestFindClosestElements(unittest.TestCase):
    def test_find_closest_elements_example1(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))

    def test_find_closest_elements_example2(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

    def test_find_closest_elements_same_numbers(self):
        self.assertEqual(find_closest_elements([1.0, 1.0, 1.0, 1.0]), (1.0, 1.0))

    def test_find_closest_elements_ascending_order(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]), (3.0, 4.0))

    def test_find_closest_elements_descending_order(self):
        self.assertEqual(find_closest_elements([5.0, 4.0, 3.0, 2.0, 1.0]), (3.0, 4.0))

    def test_find_closest_elements_duplicates(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 2.0, 2.0, 3.0]), (2.0, 2.0))

    def test_find_closest_elements_negative_numbers(self):
        self.assertEqual(find_closest_elements([-5.0, -4.0, -3.0, -2.0, -1.0]), (-4.0, -3.0))

    def test_find_closest_elements_mixed_numbers(self):
        self.assertEqual(find_closest_elements([-1.0, 0.0, 1.0, 2.0, 3.0]), (0.0, 1.0))

    def test_find_closest_elements_large_numbers(self):
        self.assertEqual(find_closest_elements([1000.0, 1001.0, 1002.0, 1003.0, 1004.0]), (1001.0, 1002.0))

if __name__ == '__main__':
    unittest.main()
