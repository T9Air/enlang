from lexer import Lexer

class Block:
    def __init__(self, block_name, code):
        self.code = code
        self.block_name = block_name
        
    def __str__(self):
        return f'BLOCK({self.block_name}, {repr(self.code)})'
    
    def __repr__(self):
        return self.__str__()
    
class Blockifier:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[0] if tokens else None
        
    def advance(self):
        self.pos += 1
        if self.pos > len(self.tokens) - 1:
            self.current_token = None
        else:
            self.current_token = self.tokens[self.pos]
    
    def blockify(self):
        blocks = [[]]
        block_names = ['1']
        name = ['1', '1']
        current_block = 0
        current_indent = 0
        
        while self.current_token:
            if self.current_token.type == 'INDENT':
                if self.current_token.value == 0:
                    current_block = 0
                    if len(name) > 2:
                        for _ in range(2, len(name)):
                            name.pop()
                elif self.current_token.value > current_indent:
                    if self.current_token.value != len(name) - 1 or ''.join(name) in block_names:
                        name[-1] = str(int(name[-1]) + 1)
                    name.append('1')
                    
                    blocks.append([])
                    block_names.append(''.join(name[:-1]))
                    blocks[current_block].append(''.join(name[:-1]))
                    for b in block_names:
                        if ''.join(name[:-1]) == b:
                            current_block = block_names.index(b)
                            break
                elif self.current_token.value < current_indent:
                    if len(name) > self.current_token.value + 2:
                        name.pop()
                    for b in block_names:    
                        check = ''.join(name[:-1])
                        if check == b:
                            current_block = block_names.index(b)
                            break
                
                current_indent = self.current_token.value
                # print("Name: ", name)
                # print("Block Names: ", block_names)
                # print("Current Block: ", current_block)
                # print("")
                self.advance()
                
            # self.advance()    
            while self.current_token and self.current_token.type != 'INDENT':
                blocks[current_block].append(self.current_token)
                self.advance()
        
        # print(block_names)
        for i, block in enumerate(blocks):
            blocks[i] = Block(block_names[i], block)
        return blocks
        
input_text = '''x is now input
    dnn
    fd
        jsdio
    sd3
        jd
            jio
ds
    jsid
sjd
'''
lexer = Lexer(input_text)
tokens = lexer.tokenize()
blockifier = Blockifier(tokens)
blocks = blockifier.blockify()
print(blocks)