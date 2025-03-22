import os
import sys

sys.path.append(os.getcwd())
sys.path.append('..')

from poly_llm.to_test.file_name_check import file_name_check

# Début de l'output du LLM
import unittest

class TestFileNameCheck(unittest.TestCase):
    def test_valid_file_name(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')

    def test_invalid_file_name_starts_with_digit(self):
        self.assertEqual(file_name_check("1example.dll"), 'No')

    def test_invalid_file_name_empty_before_dot(self):
        self.assertEqual(file_name_check(".txt"), 'No')

    def test_invalid_file_name_no_dot(self):
        self.assertEqual(file_name_check("example"), 'No')

    def test_invalid_file_name_two_dots(self):
        self.assertEqual(file_name_check("example.txt.dll"), 'No')

    def test_invalid_file_name_invalid_extension(self):
        self.assertEqual(file_name_check("example.pdf"), 'No')

    def test_invalid_file_name_more_than_three_digits(self):
        self.assertEqual(file_name_check("example1234.txt"), 'No')

    def test_valid_file_name_with_digits(self):
        self.assertEqual(file_name_check("example123.txt"), 'Yes')

    def test_valid_file_name_with_uppercase_letter(self):
        self.assertEqual(file_name_check("Example.txt"), 'Yes')

    def test_valid_file_name_with_exe_extension(self):
        self.assertEqual(file_name_check("example.exe"), 'Yes')

    def test_valid_file_name_with_dll_extension(self):
        self.assertEqual(file_name_check("example.dll"), 'Yes')

if __name__ == '__main__':
    unittest.main()
