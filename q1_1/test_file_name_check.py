import os
import sys

sys.path.append(os.getcwd())
sys.path.append('..')

from poly_llm.to_test.file_name_check import file_name_check

# Début d'ouput du LLM
import unittest

class TestFileNameCheckFunction(unittest.TestCase):

    def test_file_name_check_valid(self):
        # Test with valid file names
        self.assertEqual(file_name_check("example.txt"), 'Yes')
        self.assertEqual(file_name_check("example.exe"), 'Yes')
        self.assertEqual(file_name_check("example.dll"), 'Yes')
        self.assertEqual(file_name_check("a1b2c3.txt"), 'Yes')
        self.assertEqual(file_name_check("a1b2c.txt"), 'Yes')

    def test_file_name_check_invalid_extension(self):
        # Test with invalid extensions
        self.assertEqual(file_name_check("example.pdf"), 'No')
        self.assertEqual(file_name_check("example.doc"), 'No')
        self.assertEqual(file_name_check("example.mp3"), 'No')

    def test_file_name_check_multiple_dots(self):
        # Test with multiple dots
        self.assertEqual(file_name_check("example.txt.exe"), 'No')
        self.assertEqual(file_name_check("example.dll.txt"), 'No')

    def test_file_name_check_empty_before_dot(self):
        # Test with empty substring before the dot
        self.assertEqual(file_name_check(".txt"), 'No')
        self.assertEqual(file_name_check(".exe"), 'No')
        self.assertEqual(file_name_check(".dll"), 'No')

    def test_file_name_check_start_with_digit(self):
        # Test with file name starting with a digit
        self.assertEqual(file_name_check("1example.txt"), 'No')
        self.assertEqual(file_name_check("123example.dll"), 'No')

    def test_file_name_check_more_than_three_digits(self):
        # Test with more than three digits
        self.assertEqual(file_name_check("a1b2c3d4.txt"), 'No')
        self.assertEqual(file_name_check("a1b2c3d4e5.dll"), 'No')

    def test_file_name_check_empty_string(self):
        # Test with empty string
        self.assertEqual(file_name_check(""), 'No')

if __name__ == '__main__':
    unittest.main()
