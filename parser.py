from lexer import Lexer
from blockifier import Blockifier, Block

# Basics
class Body:
    def __init__(self, statements):
        self.statements = statements
    
    def __str__(self):
        result = f'{self.statements}'
        return result
    
    def __repr__(self):
        return self.__str__()
        
    def __iter__(self):
        return iter(self.statements)
        
    def __len__(self):
        return len(self.statements)
        
    def __getitem__(self, index):
        return self.statements[index]
class Number:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'NUMBER({self.value})'
    def __repr__(self):
        return self.__str__()
class Variable:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'VARIABLE({self.name})'
    def __repr__(self):
        return self.__str__()
class String:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'STRING({self.value})'
    def __repr__(self):
        return self.__str__()
class Boolean:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'BOOLEAN({self.value})'
    def __repr__(self):
        return self.__str__()
class Function:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'FUNCTION({self.name})'
    def __repr__(self):
        return self.__str__()
class Keyword:
    def __init__(self, value):
        self.value = value
    def __str__(self, indent=0):
        return  f"KeywordOP: {self.value}"
    def __repr__(self):
        return self.__str__()
class Condition:
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
    def __str__(self):
        return f'Condition: {self.left.__str__()} {self.op} {self.right.__str__()}'
    def __repr__(self):
        return self.__str__()
# Operations
class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op
    def __str__(self):
        return f'BinOp: {self.left.__str__()} {self.op} {self.right.__str__()}'
    def __repr__(self):
        return self.__str__()
class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __str__(self):
        return f'Assign: {self.name} = {self.value.__str__()}'
    def __repr__(self):
        return self.__str__()
class Print:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Print: {self.value.__str__()}'
    def __repr__(self):
        return self.__str__()
class Input:
    def __init__(self, var_name):
        self.var_name = var_name
    def __str__(self):
        return f'Input: {self.var_name}'
    def __repr__(self):
        return self.__str__()
class Random:
    def __init__(self, max, min):
        self.min = max
        self.max = min
    def __str__(self):
        return f'Random: min: {self.min} max: {self.max}'
    def __repr__(self):
        return self.__str__()
class IfElse:
    def __init__(self, condition, if_block, else_block = None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block
    def __str__(self):
        result = f'IfElse: {self.condition.__str__()}'
        result += f'        If Block: {self.if_block.__str__()}'
        if self.else_block:
            result += f'        Else Block: {self.else_block.__str__()}'
        return result
    def __repr__(self):
        return self.__str__()
class ForLoop:
    def __init__(self, count, body):
        self.count = count
        self.body = body
    def __str__(self):
        result = f'ForLoop: Amount: {self.count.__str__()}'
        result += f'         Body: {self.body.__str__()}'
        return result
    def __repr__(self):
        return self.__str__()
class WhileLoop:
    def __init__(self, left, op, right, body):
        self.left = left
        self.op = op
        self.right = right
        self.body = body
    def __str__(self):
        result = f'WhileLoop: Condition: {self.left.__str__()} {self.op} {self.right.__str__()}'
        result += f'           Body: {self.body.__str__()}'
        return result
    def __repr__(self):
        return self.__str__()    
class CreateFunction:
    def __init__(self, name, body):
        self.name = name
        self.body = body
    def __str__(self):
        result = f'CreateFunction: {self.name}'
        result += f'               Body: {self.body.__str__()}'
        return result
    def __repr__(self):
        return self.__str__()
class RunFunction:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'RunFunction: {self.name}'
    def __repr__(self):
        return self.__str__()

class Parser:
    def __init__(self, blocks):
        self.blocks = blocks  
        self.token_pos = 0
        self.block_pos = len(self.blocks) - 1
        self.current_block = self.blocks[self.block_pos]
        self.current_token = self.current_block.code[self.token_pos]
    def advance(self):
        self.token_pos += 1
        if self.token_pos >= len(self.current_block.code):
            self.token_pos = 0
            self.block_pos -= 1
            if self.block_pos == -1:
                self.current_block = None
                return
            self.current_block = self.blocks[self.block_pos]
        self.current_token = self.current_block.code[self.token_pos]
    def get_term(self):
        token = self.current_token
        if isinstance(token, str):
            return self.current_token
        elif self.current_token.type == 'KEYWORD':
            token = self.current_token
            self.advance()
            return Keyword(token.value)
        else:
            match token.type:
                case 'NUMBER':
                    self.advance()
                    return Number(token.value)
                case 'VARIABLE':
                    self.advance()
                    return Variable(token.value)
                case 'STRING':
                    self.advance()
                    return String(token.value)
                case 'BOOLEAN':
                    self.advance()
                    return Boolean(token.value)
                case 'FUNCTION':
                    self.advance()
                    return Function(token.value)
                case 'OPERATOR':
                    self.advance()
                    return token.value
                case 'COMPARE':
                    self.advance()
                    return token.value             
    def parse_blocks(self):
        global ast
        ast = []
        while self.current_block:
            if self.current_block.block_name == '11':
                self.token_pos = -1
                remove_first = True
            else:
                remove_first = False
            ast_block = self.parse_block()
            if remove_first == True:
                ast_block.code = ast_block.code[1:]
            ast.append(ast_block)
        final_block = ast[-1]
        final_block = final_block.code
        ast = final_block
        return Body(ast)
    def parse_block(self):
        block_num = self.block_pos
        block = []
        while self.current_token and self.block_pos == block_num:
            if isinstance(self.current_token, str):
                block.append(self.current_token)
                self.advance()
                continue
            elif self.current_token.type == 'NEWLINE':
                self.advance()
                continue
            line = self.parse_expression()
            if line:
                block.append(line)
        this_block = self.blocks[self.block_pos + 1]
        return Block(this_block.block_name, Body(block))
    
    def parse_expression(self):
        left = self.get_term()
        if isinstance(left, Keyword):
            match left.value:
                case 'print':
                    right = self.get_term()
                    if self.current_token.type == 'NUMBER' or self.current_token.type == 'VARIABLE':
                        if self.current_token.type == 'OPERATOR':
                            op = self.current_token.value
                            self.advance()
                            next = self.get_term()
                            right = BinOp(right, op, next)
                    elif self.current_token.type == 'KEYWORD':
                        if self.current_token.value == 'random':
                            self.advance()
                            min = self.get_term()
                            max = self.get_term()
                            right = Random(min, max)
                    left = Print(right)
                case 'if':
                    right = self.get_term()
                    comparison = self.get_term()
                    left = self.get_term()
                    condition = Condition(right, left, comparison)
                    self.advance()
                    for block in ast:
                        if block.block_name == self.current_token:
                            if_block = Body(block.code)
                    self.advance()
                    yes = self.get_term()
                    if isinstance(yes, Keyword) and yes.value == 'else':
                        else_block = None
                        self.advance()
                        for block in ast:
                            if block.block_name == self.current_token:
                                else_block = Body(block.code)
                        self.advance()
                        left = IfElse(condition, if_block, else_block)
                    else:
                        left = IfElse(condition, if_block)
                case 'for_loop':
                    right = self.get_term()
                    self.advance()
                    for block in ast:
                        if block.block_name == self.current_token:
                            body = Body(block.code)
                    left = ForLoop(right, body)
                    self.advance()
                case 'while_loop':
                    left = self.get_term()
                    comparison = self.get_term()
                    right = self.get_term()
                    self.advance()
                    for block in ast:
                        if block.block_name == self.current_token:
                            body = Body(block.code)
                    self.advance()
                    left = WhileLoop(left, comparison, right, body)
                case 'create_function':
                    right = self.get_term()
                    self.advance()
                    for block in ast:
                        if block.block_name == self.current_token:
                            body = Body(block.code)
                    left = CreateFunction(right, body)
                    self.advance()
                case 'run_function':
                    right = self.get_term()
                    left = RunFunction(right)
                case 'assign':
                    name = self.current_block.code[self.token_pos - 2]
                    name = name.value
                    right = self.get_term()
                    if isinstance(right, Keyword):
                        if right.value == 'input':
                            right = Input(left.name)
                        elif right.value == 'random':
                            min = self.get_term()
                            max = self.get_term()
                            right = Random(min, max)
                    elif self.current_token and self.current_token.type == 'OPERATOR':
                        op = self.current_token.value
                        self.advance()
                        next_num = self.get_term()
                        right = BinOp(right, op, next_num)
                    elif isinstance(right, Boolean):
                        right = Boolean(right.value)
                    left = Assign(name, right)

        elif left:
            if self.current_token.type == 'OPERATOR':
                op = self.get_term()
                right = self.get_term()
                left = BinOp(left, op, right)
            elif self.current_token.type == 'KEYWORD':
                if self.current_token.value == 'assign':
                    self.advance()
                    right = self.get_term()
                    if isinstance(right, Keyword):
                        if right.value == 'input':
                            right = Input(left.name)
                        elif right.value == 'random':
                            min = self.get_term()
                            max = self.get_term()
                            right = Random(min, max)
                    elif self.current_token and self.current_token.type == 'OPERATOR':
                        op = self.current_token.value
                        self.advance()
                        next_num = self.get_term()
                        right = BinOp(right, op, next_num)
                    elif isinstance(right, Boolean):
                        right = Boolean(right.value)
                    left = Assign(left.name, right)
                    
        return left

if __name__ == '__main__':
    input_text = '''
repeat until x = 9
    output "56"
'''
    lexer = Lexer(input_text)
    tokens = lexer.tokenize()
    blockifier = Blockifier(tokens)
    blocks = blockifier.blockify()
    parser = Parser(blocks)
    parsed_blocks = parser.parse_blocks()
    print(parsed_blocks)