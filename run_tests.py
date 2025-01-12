from lexer import Lexer
from blockifier import Blockifier
from parser import Parser
from interpreter import Interpreter
import os
import random  # Added for generating random inputs
import msvcrt  # for Windows systems
from datetime import datetime

def run_test(file_path, test_input):
    with open(file_path, 'r') as file:
        input_text = file.read()
    
    lexer = Lexer(input_text)
    tokens = lexer.tokenize()
    blockifier = Blockifier(tokens)
    blocks = blockifier.blockify()
    parser = Parser(blocks)
    parsed_blocks = parser.parse_blocks()
    interpreter = Interpreter(parsed_blocks, True, test_input)
    interpreter.interpret()
    return interpreter.test_output

def save_test_results(test_name, test_output, result_file):
    results_dir = 'test_results'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    with open(result_file, 'a') as f:
        f.write(f"\nTest Results for {test_name}\n")
        f.write("=" * 50 + "\n")
        for output in test_output:
            f.write(f"{output}\n")
        f.write("\n")

def wait_key():
    print("\nPress any key to continue...")
    msvcrt.getch()

def generate_inputs(count=10):
    return [random.randint(1, 100) for _ in range(count)]

def main():
    # Define all test files
    test_files = [
        'arithmetic_test.enl',
        'comparison_test.enl',
        'function_test.enl',
        'loops_test.enl',
        'output_test.enl',
        'variables_test.enl',
        'guessing_game_test.enl',
        'loops_test.enl',
        'temperature_converter.enl',
        'counter_test.enl'
    ]
    
    test_dir = 'Code_Tests'
    
    # Generate 10 random inputs
    test_inputs = generate_inputs()
    
    # Define a unique test results file with date and time
    results_dir = 'test_results'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    result_file = os.path.join(results_dir, f'{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(result_file, 'a') as f:
        f.write(f"Test Results for {timestamp}\n")
        f.write("=" * 50 + "\n")
        f.write(f"Test Inputs: {test_inputs}\n")
        f.write("=" * 50 + "\n")
        f.close()
    
    # Run all tests in testing mode
    for test_file in test_files:
        file_path = os.path.join(test_dir, test_file)
        try:
            test_output = run_test(file_path, test_inputs)
            save_test_results(test_file.replace('.enl', ''), test_output, result_file)
        except Exception as e:
            save_test_results(test_file.replace('.enl', ''), [f"Error: {str(e)}"], result_file)
    
    # No terminal output
    # ...existing code...
    
if __name__ == "__main__":
    main()
