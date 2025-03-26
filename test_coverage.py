from poly_llm.common.abstract_executor import AbstractExecutor

from poly_llm.to_test.file_name_check import test_file_name_check
from poly_llm.to_test.closest_integer import test_closest_integer
from poly_llm.to_test.find_closest_elements import test_find_closest_elements
from poly_llm.to_test.numerical_letter_grade import test_numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import test_separate_paren_groups

def _get_coverage(test_function):
    executor = AbstractExecutor(test_function)
    
    return executor._execute_input()

def get_all_files_coverage():
    print(_get_coverage(test_closest_integer))
    print(_get_coverage(test_file_name_check))
    print(_get_coverage(test_find_closest_elements))
    print(_get_coverage(test_numerical_letter_grade))
    print(_get_coverage(test_separate_paren_groups))

if __name__ == '__main__':
    get_all_files_coverage()
