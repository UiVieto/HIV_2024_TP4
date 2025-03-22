import os
import sys

sys.path.append(os.getcwd())
sys.path.append('..')

from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade

# Début d'ouput du LLM
import unittest

class TestNumericalLetterGradeFunction(unittest.TestCase):

    def test_numerical_letter_grade_a_plus(self):
        # Test with GPA 4.0
        self.assertEqual(numerical_letter_grade([4.0]), ['A+'])

    def test_numerical_letter_grade_a(self):
        # Test with GPA greater than 3.7
        self.assertEqual(numerical_letter_grade([3.8]), ['A'])
        self.assertEqual(numerical_letter_grade([3.71]), ['A'])

    def test_numerical_letter_grade_a_minus(self):
        # Test with GPA greater than 3.3
        self.assertEqual(numerical_letter_grade([3.4]), ['A-'])
        self.assertEqual(numerical_letter_grade([3.31]), ['A-'])

    def test_numerical_letter_grade_b_plus(self):
        # Test with GPA greater than 3.0
        self.assertEqual(numerical_letter_grade([3.1]), ['B+'])
        self.assertEqual(numerical_letter_grade([3.01]), ['B+'])

    def test_numerical_letter_grade_b(self):
        # Test with GPA greater than 2.7
        self.assertEqual(numerical_letter_grade([2.8]), ['B'])
        self.assertEqual(numerical_letter_grade([2.71]), ['B'])

    def test_numerical_letter_grade_b_minus(self):
        # Test with GPA greater than 2.3
        self.assertEqual(numerical_letter_grade([2.4]), ['B-'])
        self.assertEqual(numerical_letter_grade([2.31]), ['B-'])

    def test_numerical_letter_grade_c_plus(self):
        # Test with GPA greater than 2.0
        self.assertEqual(numerical_letter_grade([2.1]), ['C+'])
        self.assertEqual(numerical_letter_grade([2.01]), ['C+'])

    def test_numerical_letter_grade_c(self):
        # Test with GPA greater than 1.7
        self.assertEqual(numerical_letter_grade([1.8]), ['C'])
        self.assertEqual(numerical_letter_grade([1.71]), ['C'])

    def test_numerical_letter_grade_c_minus(self):
        # Test with GPA greater than 1.3
        self.assertEqual(numerical_letter_grade([1.4]), ['C-'])
        self.assertEqual(numerical_letter_grade([1.31]), ['C-'])

    def test_numerical_letter_grade_d_plus(self):
        # Test with GPA greater than 1.0
        self.assertEqual(numerical_letter_grade([1.1]), ['D+'])
        self.assertEqual(numerical_letter_grade([1.01]), ['D+'])

    def test_numerical_letter_grade_d(self):
        # Test with GPA greater than 0.7
        self.assertEqual(numerical_letter_grade([0.8]), ['D'])
        self.assertEqual(numerical_letter_grade([0.71]), ['D'])

    def test_numerical_letter_grade_d_minus(self):
        # Test with GPA greater than 0.0
        self.assertEqual(numerical_letter_grade([0.1]), ['D-'])
        self.assertEqual(numerical_letter_grade([0.01]), ['D-'])

    def test_numerical_letter_grade_e(self):
        # Test with GPA 0.0 or less
        self.assertEqual(numerical_letter_grade([0.0]), ['E'])
        self.assertEqual(numerical_letter_grade([-1.0]), ['E'])

    def test_numerical_letter_grade_multiple(self):
        # Test with multiple GPAs
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ['A+', 'B', 'C', 'C', 'A-'])

if __name__ == '__main__':
    unittest.main()
