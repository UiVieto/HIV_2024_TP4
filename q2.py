import json
import importlib

from transformers import AutoTokenizer, T5ForConditionalGeneration
import torch

from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator

from poly_llm.to_test.closest_integer import closest_integer
from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.to_test.find_closest_elements import find_closest_elements
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import separate_paren_groups


FUNCTIONS_TO_TEST = [
    (closest_integer, 'closest_integer', [
        """def test_closest_integer(): \n assert closest_integer("10") == 10"""
    ]),
    (file_name_check, 'file_name_check', [
        """def test_file_name_check(): \n
        assert file_name_check("example.txt") == 'Yes'"""
    ]),
    (find_closest_elements, 'find_closest_elements', [
        """def test_find_closest_elements(): \n
        assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)"""
    ]),
    (numerical_letter_grade, 'numerical_letter_grade', [
        """def test_numerical_letter_grade(): \n
        assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']"""
    ]),
    (separate_paren_groups, 'separate_paren_groups', [
        """def test_separate_paren_groups(): \n
        assert separate_paren_groups('(()()) ((())) () ((())()())') == [
            '(()())', '((()))', '()', '((())()())'
        ]"""
    ])
]
#MODEL_NAME = "Salesforce/codet5-large-ntp-py"

#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
#model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)

def test_function(function, examples: list[str] | None=None) -> tuple[dict, dict]:
    executor = AbstractExecutor(function)
    prompt_generator = PromptGenerator(function)

    # llm_generator = LLMTestGenerator(model, tokenizer, function)
    prompt = prompt_generator.generate_prompt(few_shot_examples=examples)

    print(f"THE PROMPT {prompt}\n")
    # test, test_name = llm_generator.create_test_function(prompt)

    filename = "test_generated.py"
    # llm_generator.write_test_to_file(test, filename=filename)

    module_name = filename.split(".")[0]
    # function_name = test_name

    # Dynamically import the module
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)

    executor = AbstractExecutor(function)

    # coverage_data = executor._execute_input(function)
    # print(coverage_data)


if __name__ == '__main__':
    for function, function_name, example in FUNCTIONS_TO_TEST:
        print(function_name)
        test_function(function, 'test')
        test_function(function, 'test', example)
