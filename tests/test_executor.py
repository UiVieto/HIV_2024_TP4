import sys
import os

# Add the root directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.common.abstract_executor import AbstractExecutor
from test_generated import test_file_name_check
import coverage
import json
def test_executor():
    executor  = AbstractExecutor(test_file_name_check) # set up the function we want to execute
    input = file_name_check # set up the input we want to pass to the function when we execute it
    coverage_data = executor._execute_input(input)
    line_coverage = coverage_data["coverage"]["covered_lines"] 
    print(line_coverage)
    cov = coverage.Coverage(branch=True)
    cov.start()
    # Execute test cases
    test_file_name_check(file_name_check)
    # Stop code coverage
    cov.stop()

    cov.json_report()
    with open("coverage.json", "r") as f:
        f = json.load(f)
    coverage_data = f["totals"]
    line_coverage2 = coverage_data["covered_lines"]
    print(line_coverage2)

    assert line_coverage == line_coverage2

test_executor()