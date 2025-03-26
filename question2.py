import json
import torch
import importlib
import pathlib

from transformers import AutoTokenizer, T5ForConditionalGeneration

from poly_llm.to_test.file_name_check import file_name_check, test_file_name_check
from poly_llm.to_test.closest_integer import closest_integer, test_closest_integer
from poly_llm.to_test.find_closest_elements import find_closest_elements, test_find_closest_elements
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade, test_numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import separate_paren_groups, test_separate_paren_groups

from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator

from test_coverage import get_all_files_coverage

PROGRAMS_UNDER_TEST = [
    (closest_integer, 'closest_integer'),
    (file_name_check, 'file_name_check'),
    (find_closest_elements, 'find_closest_elements'),
    (numerical_letter_grade, 'numerical_letter_grade'),
    (separate_paren_groups, 'separate_paren_groups')
]

Q_2_3_TEST_INPUTS = [
    ["""def test_closest_integer(): \n assert closest_integer("10") == 10 \n"""],
    ["""def test_file_name_check(): \n assert file_name_check("example.txt") == 'Yes'\n"""],
    ["""def test_find_closest_elements(): \n assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)\n"""],
    ["""def test_numerical_letter_grade(): \n assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']\n"""],
    ["""def test_separate_paren_groups(): \n assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']\n"""]
]

Q_2_4_TEST_INPUTS_2 = [
    [
        """def test_closest_integer(): \n assert closest_integer("0.2") == 0 \n""",
        """def test_closest_integer(): \n assert closest_integer("-1.9") == -2 \n"""
    ],
    [
        """def test_file_name_check(): \n assert file_name_check("example.txt") == 'Yes'\n"""
        """def test_file_name_check(): \n assert file_name_check("example") == 'No'\n"""
    ],
    [
        """def test_find_closest_elements(): \n assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)\n"""
        """def test_find_closest_elements(): \n assert find_closest_elements([1.0, 1.0]) == (1.0, 1.0)\n"""
    ],
    [
        """def test_numerical_letter_grade(): \n assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']\n""",
        """def test_numerical_letter_grade(): \n assert numerical_letter_grade([0.75, 0.1, 0.0]) == ['D', 'D-', 'E']\n"""
    ],
    [
        """def test_separate_paren_groups(): \n assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']\n"""
        """def test_separate_paren_groups(): \n assert separate_paren_groups('((()))') == ['((()))']\n"""
    ]
]

Q_2_4_TEST_INPUTS_1 = [
    [
        """def test_closest_integer(): \n assert closest_integer("0.5") == 1 \n""",
        """def test_closest_integer(): \n assert closest_integer("-1.9") == -2 \n"""
    ],
    [
        """def test_file_name_check(): \n assert file_name_check("example.txt") == 'Yes'\n"""
        """def test_file_name_check(): \n assert file_name_check("fail.12") == 'No'\n"""
    ],
    [
        """def test_find_closest_elements(): \n assert find_closest_elements([1.0, 2.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)\n"""
        """def test_find_closest_elements(): \n assert find_closest_elements([1.0, 1.0]) == (1.0, 1.0)\n"""
    ],
    [
        """def test_numerical_letter_grade(): \n assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']\n""",
        """def test_numerical_letter_grade(): \n assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5, 0.75, 0.1, 0.0]) == ['A+', 'B', 'C-', 'C', 'A-', 'D', 'D-', 'E']\n"""
    ],
    [
        """def test_separate_paren_groups(): \n assert separate_paren_groups('(()()) ((())) ()') == ['(()())', '((()))', '()']\n"""
        """def test_separate_paren_groups(): \n assert separate_paren_groups('() ((())) ()') == ['() ((())) ()']\n"""
    ]
]


Q_2_4_TEST_INPUTS_3 = [
    [
        """def test_closest_integer(): \n assert closest_integer("0.0") == 0 \n""",
        """def test_closest_integer(): \n assert closest_integer("-100.123124") == -100 \n"""
    ],
    [
        """def test_file_name_check(): \n assert file_name_check("giubfvaewovbaw.dll") == 'Yes'\n"""
        """def test_file_name_check(): \n assert file_name_check("wadawfsvwe.12") == 'No'\n"""
    ],
    [
        """def test_find_closest_elements(): \n assert find_closest_elements([1.0, 2.0, 40.0, 5.0, 2.2]) == (2.0, 2.2)\n"""
        """def test_find_closest_elements(): \n assert find_closest_elements([1.0, 1231.23, 2.0]) == (1.0, 2.0)\n"""
    ],
    [
        """def test_numerical_letter_grade(): \n assert numerical_letter_grade([4.0, 3, 1.7]) == ['A+', 'B', 'C-']\n""",
        """def test_numerical_letter_grade(): \n assert numerical_letter_grade([4.0, 3, 3.5, 0.75, 0.1, 0.0]) == ['A+', 'B', 'A-', 'D', 'D-', 'E']\n"""
    ],
    [
        """def test_separate_paren_groups(): \n assert separate_paren_groups('(()()) ()') == ['(()())', '()']\n"""
        """def test_separate_paren_groups(): \n assert separate_paren_groups('() ((())) ()') == ['() ((())) ()']\n"""
    ]
]

def generate_inputs(module, tokenizer, model, output_file: str, inputs: list[str] | None=None):
    if not pathlib.Path(output_file).is_file():
        prompt_generator = PromptGenerator(module)
        llm_generator = LLMTestGenerator(model, tokenizer, module)

        prompt = prompt_generator.generate_prompt(inputs)
        print(f'PROMPT: {prompt}')

        test, _ = llm_generator.create_test_function(prompt)

        llm_generator.write_test_to_file(test, filename=output_file)
    else:
        print(f'File {output_file} already exists: Skipping input generation.')


if __name__ == '__main__':
    # Génère les couvertures pour les tests pour chaque fichier
    get_all_files_coverage()

    # Génère les inputs à ajouter aux fichiers
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_name = "Salesforce/codet5-large-ntp-py"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

    print("Q2.2 - Génération d'inputs zéro shot")
    for function, function_name in PROGRAMS_UNDER_TEST:
        print(f"Zero Shot: {function_name}.....................................")
        print(generate_inputs(function, tokenizer, model, f'zero_test_{function_name}.py', None))

    print("Q2.3 - Génération d'inputs few shot")
    for i, (function, function_name) in enumerate(PROGRAMS_UNDER_TEST):
        print(f"Few Shot: {function_name}......................................")
        generate_inputs(
            function, tokenizer, model, f'few_test_{function_name}.py',
            Q_2_3_TEST_INPUTS[i]    
        )

    print("Q2.4 - Génération d'inputs few shot")
    for i, (function, function_name) in enumerate(PROGRAMS_UNDER_TEST):
        print(f"Few Shot: {function_name}......................................")
        generate_inputs(
            function, tokenizer, model, f'q241_few_test_{function_name}.py',
            Q_2_4_TEST_INPUTS_1[i]    
        )

    for i, (function, function_name) in enumerate(PROGRAMS_UNDER_TEST):
        print(f"Few Shot: {function_name}......................................")
        generate_inputs(
            function, tokenizer, model, f'q242_few_test_{function_name}.py',
            Q_2_4_TEST_INPUTS_2[i]    
        )

    for i, (function, function_name) in enumerate(PROGRAMS_UNDER_TEST):
        print(f"Few Shot: {function_name}......................................")
        generate_inputs(
            function, tokenizer, model, f'q243_few_test_{function_name}.py',
            Q_2_4_TEST_INPUTS_3[i]    
        )
