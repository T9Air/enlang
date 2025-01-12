import sys
import subprocess
from lexer import Lexer
from blockifier import Blockifier
from parser import Parser
from interpreter import Interpreter

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_file.py <filename>")
        return
    filename = sys.argv[1]
    if not filename.endswith('.enl'):
        print("Please provide a .enl file.")
        return
    with open(filename, 'r') as f:
        code = f.read()
    tokens = Lexer(code).tokenize()
    blocks = Blockifier(tokens).blockify()
    ast = Parser(blocks).parse_blocks()
    Interpreter(ast).interpret()

if __name__ == "__main__":
    main()
