import os
import sys

sys.path.append(os.getcwd())
sys.path.append('..')

from poly_llm.to_test.separate_paren_groups import separate_paren_groups

# Début de l'output du LLM
import unittest
# from separate_paren_groups import separate_paren_groups <- Mauvais import

class TestSeparateParenGroups(unittest.TestCase):
    def test_separate_paren_groups_example(self):
        self.assertEqual(separate_paren_groups('(()()) ((())) () ((())()())'), [
            '(()())', '((()))', '()', '((())()())'
        ])

    def test_separate_paren_groups_multiple_groups(self):
        self.assertEqual(separate_paren_groups('() (()) ((())) (((())))'), [
            '()', '(())', '((()))', '(((())))'
        ])

    def test_separate_paren_groups_single_group(self):
        self.assertEqual(separate_paren_groups('()'), [
            '()'
        ])

    def test_separate_paren_groups_empty_string(self):
        self.assertEqual(separate_paren_groups(''), [
        ])

    def test_separate_paren_groups_no_groups(self):
        self.assertEqual(separate_paren_groups('abcdefg'), [
        ])

    def test_separate_paren_groups_nested_groups(self):
        self.assertEqual(separate_paren_groups('((()))'), [
            '((()))'
        ])

    def test_separate_paren_groups_consecutive_groups(self):
        self.assertEqual(separate_paren_groups('()()()'), [
            '()', '()', '()'
        ])

    def test_separate_paren_groups_ignores_spaces(self):
        self.assertEqual(separate_paren_groups(' ( () ) ( ( () ) ) '), [
            '()', '(())'
        ])

    def test_separate_paren_groups_unbalanced_parens(self):
        with self.assertRaises(ValueError):
            separate_paren_groups('(()')

    def test_separate_paren_groups_empty_group(self):
        self.assertEqual(separate_paren_groups('()'), [
            '()'
        ])

if __name__ == '__main__':
    unittest.main()