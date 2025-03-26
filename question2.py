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

def get_coverage(test_function):
    executor = AbstractExecutor(test_function)
    
    return executor._execute_input()

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

def generate_coverage(module, output_file: str, test_name: str):
    module_name = output_file.split(".")[0]
    function_name = test_name

    # Dynamically import the module
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)

    executor = AbstractExecutor(function)

    return executor._execute_input(module)


if __name__ == '__main__':
    # Génère les couvertures pour les tests pour chaque fichier
    print(get_coverage(test_closest_integer))
    print(get_coverage(test_file_name_check))
    print(get_coverage(test_find_closest_elements))
    print(get_coverage(test_numerical_letter_grade))
    print(get_coverage(test_separate_paren_groups))

    # Génère les inputs à ajouter aux fichiers
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_name = "Salesforce/codet5-large-ntp-py"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

    print("Génération d'inputs zéro shot")
    print("Zero Shot: file_name_check.....................................")
    print(generate_inputs(file_name_check, tokenizer, model, 'z_llm_file_name_check.py', None))

    print("Zero Shot: closest_integer.....................................")
    print(generate_inputs(closest_integer, tokenizer, model, 'z_test_closest_integer.py', None))

    print("Zero Shot: find_closest_elements...............................")
    print(generate_inputs(find_closest_elements, tokenizer, model, 'z_test_find_closest_elements.py', None))

    print("Zero Shot: numerical_letter_grade..............................")
    print(generate_inputs(numerical_letter_grade, tokenizer, model, 'z_test_numerical_letter_grade.py', None))

    print("Zero Shot: separate_paren_groups...............................")
    print(generate_inputs(separate_paren_groups, tokenizer, model, 'z_test_separate_paren_groups.py', None))


    print("Génération d'inputs few shot")
    print("Few Shot: file_name_check......................................")
    print(generate_inputs(
        file_name_check, tokenizer, model, 'f_llm_file_name_check.py',
        ["""def test_file_name_check(): \n assert file_name_check("example.txt") == 'Yes'\n"""]    
    ))

    print("Few Shot: closest_integer......................................")
    print(generate_inputs(
        closest_integer, tokenizer, model, 'f_test_closest_integer.py',
        ["""def test_closest_integer(): \n assert closest_integer("10") == 10 \n"""]
    ))

    print("Few Shot: find_closest_elements................................")
    print(generate_inputs(
        find_closest_elements, tokenizer, model, 'f_test_find_closest_elements.py',
        ["""def test_find_closest_elements(): \n assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)\n"""]        
    ))

    print("Few Shot: numerical_letter_grade...............................")
    print(generate_inputs(
        numerical_letter_grade, tokenizer, model, 'f_test_numerical_letter_grade.py',
        ["""def test_numerical_letter_grade(): \n assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']\n"""]        
    ))

    print("Few Shot: separate_paren_groups................................")
    print(generate_inputs(
        separate_paren_groups, tokenizer, model, 'f_test_separate_paren_groups.py',
        ["""def test_separate_paren_groups(): \n assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']\n"""]        
    ))
