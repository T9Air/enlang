class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {repr(self.value)})'

    def __repr__(self):
        return self.__str__()
    
class Lexer:
    def __init__(self, text):
        self.text = []
        lines = text.split('\n')
        for line in lines:
            line = line.rstrip()
            if line != '':
                self.text.append('\n')
                self.text.append(line)
        self.text = '\n'.join(self.text)
        self.pos = 0
        self.current_char = self.text[0] if text else None

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def unadvance(self):
        self.pos -= 1
        self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            if self.current_char == '\n':
                self.advance()
                return Token('NEWLINE', '\n')
            self.advance()
        return None

    def get_number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def get_identifier(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        return result
    
    def get_string(self):
        self.advance()
        result = ''
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()
        return result
    
    def tokenize(self):
        tokens = []
        
        while self.current_char:
            if self.current_char.isspace():
                if self.current_char == '\n':
                    if self.pos != 0:
                        tokens.append(Token('NEWLINE', '\n'))
                    spaces = 0
                    while self.current_char and self.current_char.isspace():
                        spaces += 1
                        self.advance()
                    self.unadvance()
                    indent_level = spaces // 4
                    tokens.append(Token('INDENT', indent_level))
                else:
                    self.skip_whitespace()
            
            elif self.current_char.isdigit():
                tokens.append(Token('NUMBER', self.get_number()))
            
            elif self.current_char == '"':
                tokens.append(Token('STRING', self.get_string()))
            
            elif self.current_char.isalpha():
                identifier = self.get_identifier()
                match identifier:
                    case 'plus':
                        tokens.append(Token('OPERATOR', '+'))
                    case 'minus':
                        tokens.append(Token('OPERATOR', '-'))
                    case 'times':
                        tokens.append(Token('OPERATOR', '*'))
                    case 'divide':
                        tokens.append(Token('OPERATOR', '/'))
                    case 'is':
                        self.skip_whitespace()
                        if self.current_char and self.current_char.isalpha():
                            identifier = self.get_identifier()
                            if identifier == 'now':
                                tokens.append(Token('KEYWORD', 'assign'))
                            else:
                                tokens.append(Token('IDENTIFIER', 'is'))
                                continue
                    case 'create':
                        tokens.append(Token('KEYWORD', 'create_function'))
                        self.skip_whitespace()
                        tokens.append(Token('FUNCTION', self.get_identifier()))
                    case 'run':
                        tokens.append(Token('KEYWORD', 'run_function'))
                        self.skip_whitespace()
                        tokens.append(Token('FUNCTION', self.get_identifier()))
                    case 'if':
                        tokens.append(Token('KEYWORD', 'if'))
                    case 'otherwise':
                        tokens.append(Token('KEYWORD', 'else'))
                    case 'output':
                        tokens.append(Token('KEYWORD', 'print'))
                    case 'input':
                        tokens.append(Token('KEYWORD', 'input'))
                    case 'repeat':
                        self.skip_whitespace()
                        if self.current_char and self.current_char.isdigit():
                            number = self.get_number()
                            self.skip_whitespace()
                            identifier = self.get_identifier()
                            if identifier == 'times':
                                tokens.append(Token('KEYWORD', 'for_loop'))
                                tokens.append(Token('NUMBER', number))
                            else:
                                tokens.append(Token('IDENTIFIER', 'repeat'))
                                tokens.append(Token('NUMBER', number))
                                tokens.append(Token('IDENTIFIER', identifier))
                        elif self.current_char and self.current_char.isalpha():
                            identifier = self.get_identifier()
                            if identifier == 'until':
                                tokens.append(Token('KEYWORD', 'while_loop'))
                                continue
                            else:
                                self.skip_whitespace()
                                next_identifier = self.get_identifier()
                                if next_identifier == 'times':
                                    tokens.append(Token('KEYWORD', 'for_loop'))
                                    tokens.append(Token('IDENTIFIER', identifier))
                                else:
                                    tokens.append(Token('IDENTIFIER', 'repeat'))
                                    tokens.append(Token('IDENTIFIER', identifier))
                        else:
                            tokens.append(Token('IDENTIFIER', 'repeat'))
                            continue
                    case _:
                        tokens.append(Token('IDENTIFIER', identifier))
            
            elif self.current_char in ['=', '>', '<', '!']:
                compare = self.current_char
                self.advance()
                if self.current_char in ['=', '>', '<', '!']:
                    compare += self.current_char
                else:
                    self.unadvance()
                
                match compare:
                    case '=' | '==':
                        tokens.append(Token('COMPARE', '=='))
                    case '!=' | '=!':
                        tokens.append(Token('COMPARE', '!='))
                    case '>=' | '=>':
                        tokens.append(Token('COMPARE', '>='))
                    case '<=' | '=<':
                        tokens.append(Token('COMPARE', '<='))
                    case '>':
                        tokens.append(Token('COMPARE', '>'))
                    case '<':
                        tokens.append(Token('COMPARE', '<'))
                    
                self.advance()
            
            self.advance()
        
        return tokens

if __name__ == '__main__':    
    input_text = '''x is now input
    '''
    lexer = Lexer(input_text)
    tokens = lexer.tokenize()
    print("Tokens:", tokens)