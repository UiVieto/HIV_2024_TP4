import os
import sys

sys.path.append(os.getcwd())
sys.path.append('..')

from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade

# Début de l'output du LLM
import unittest

class TestNumericalLetterGrade(unittest.TestCase):
    def test_numerical_letter_grade_example(self):
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ['A+', 'B', 'C-', 'C', 'A-'])

    def test_numerical_letter_grade_single_gpa(self):
        self.assertEqual(numerical_letter_grade([1.2]), ['D+'])

    def test_numerical_letter_grade_a_plus(self):
        self.assertEqual(numerical_letter_grade([4.0]), ['A+'])

    def test_numerical_letter_grade_a(self):
        self.assertEqual(numerical_letter_grade([3.8]), ['A'])

    def test_numerical_letter_grade_a_minus(self):
        self.assertEqual(numerical_letter_grade([3.4]), ['A-'])

    def test_numerical_letter_grade_b_plus(self):
        self.assertEqual(numerical_letter_grade([3.1]), ['B+'])

    def test_numerical_letter_grade_b(self):
        self.assertEqual(numerical_letter_grade([2.8]), ['B'])

    def test_numerical_letter_grade_b_minus(self):
        self.assertEqual(numerical_letter_grade([2.4]), ['B-'])

    def test_numerical_letter_grade_c_plus(self):
        self.assertEqual(numerical_letter_grade([2.1]), ['C+'])

    def test_numerical_letter_grade_c(self):
        self.assertEqual(numerical_letter_grade([1.8]), ['C'])

    def test_numerical_letter_grade_c_minus(self):
        self.assertEqual(numerical_letter_grade([1.4]), ['C-'])

    def test_numerical_letter_grade_d_plus(self):
        self.assertEqual(numerical_letter_grade([1.1]), ['D+'])

    def test_numerical_letter_grade_d(self):
        self.assertEqual(numerical_letter_grade([0.8]), ['D'])

    def test_numerical_letter_grade_d_minus(self):
        self.assertEqual(numerical_letter_grade([0.1]), ['D-'])

    def test_numerical_letter_grade_e(self):
        self.assertEqual(numerical_letter_grade([0.0]), ['E'])

    def test_numerical_letter_grade_empty_list(self):
        self.assertEqual(numerical_letter_grade([]), [])

    def test_numerical_letter_grade_multiple_gpas(self):
        self.assertEqual(numerical_letter_grade([4.0, 3.7, 1.7, 2.3, 3.5]), ['A+', 'A', 'C-', 'B-', 'A-'])

if __name__ == '__main__':
    unittest.main()