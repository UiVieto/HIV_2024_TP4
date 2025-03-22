import os
import sys

sys.path.append(os.getcwd())
sys.path.append('..')

from poly_llm.to_test.separate_paren_groups import separate_paren_groups

# Début d'ouput du LLM
import unittest
from typing import List

class TestSeparateParenGroupsFunction(unittest.TestCase):

    def test_separate_paren_groups_single_group(self):
        # Test with a single group of parentheses
        self.assertEqual(separate_paren_groups('( )'), ['()'])

    def test_separate_paren_groups_multiple_groups(self):
        # Test with multiple groups of parentheses
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

    def test_separate_paren_groups_nested_groups(self):
        # Test with nested groups of parentheses
        self.assertEqual(separate_paren_groups('( ( ) )'), ['(())'])

    def test_separate_paren_groups_empty_string(self):
        # Test with an empty string
        self.assertEqual(separate_paren_groups(''), [])

    def test_separate_paren_groups_no_parentheses(self):
        # Test with a string containing no parentheses
        self.assertEqual(separate_paren_groups('hello world'), [])

    def test_separate_paren_groups_spaces(self):
        # Test with a string containing spaces
        self.assertEqual(separate_paren_groups(' ( ) (( )) (( )( )) '), ['()', '(())', '(()())'])

    def test_separate_paren_groups_unbalanced_parentheses(self):
        # Test with unbalanced parentheses
        with self.assertRaises(ValueError):
            separate_paren_groups('( ) (( )')

    def test_separate_paren_groups_large_input(self):
        # Test with a large input string
        large_input = '( ) (( )) (( )( ))'* 100
        expected_output = ['()', '(())', '(()())'] * 100
        self.assertEqual(separate_paren_groups(large_input), expected_output)

if __name__ == '__main__':
    unittest.main()
