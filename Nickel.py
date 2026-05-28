import argparse
import sys

parser = argparse.ArgumentParser(description='Interpret nc files')
parser.add_argument('filename', help='a .nc language file')
args = parser.parse_args()

if not args.filename.endswith('.nc'):
    parser.error('filename must end with .nc')


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


class NumNode:
    def __init__(self, val):
        self.value = val

    def __repr__(self):
        return f"NumNode({self.value})"
    
class BinOptNode:
    def __init__(self, val, left, right):
        self.right = right
        self.left = left
        self.value = val

    def __repr__(self):
        return f"BinOptNode({self.value}, {self.left}, {self.right})"



def tokenize(script):
    tokens = []
    i = 0
    
    while i < len(script):
        char = script[i]
        if char.isspace():
            i += 1
            continue

        if char.isdigit():
            # Accumulate all consecutive digits
            num_str = ""
            while i < len(script) and (script[i].isdigit() or script[i] == '.'):
                num_str += script[i]
                i += 1
            tokens.append(Token("NUMBER", float(num_str)))
            continue  # Don't increment i again
        elif char == '+':
            tokens.append(Token("PLUS", char))
        elif char == '-':
            tokens.append(Token("MINUS", char))
        elif char == '/':
            tokens.append(Token("SLASH", char))
        elif char == '*':
            tokens.append(Token("STAR", char))
        elif char == '(':
            tokens.append(Token("LPAREN", char))
        elif char == ')':
            tokens.append(Token("RPAREN", char))
        elif char.isalpha():
            word = ""
            while i < len(script) and script[i].isalpha():  # <-- ADD THIS
             word += script[i]
             i += 1
            if word == "let":
                tokens.append(Token("LET", word))
            else:
                tokens.append(Token("NAME", word))
                continue
        elif char == '=':
            tokens.append(Token("EQUALS", char))

        i += 1
    return tokens

def ast_parse(tokens):
    # Pass 1: Handle * and /
    if tokens[0].type == "LET":
        env[tokens[1].value] = tokens[3].value
    elif tokens[0].type == "NAME" and tokens[1].type == "EQUALS":
        env[tokens[0].value] = evaluate(ast_parse(tokens[2:]))
    pass1 = []
    i = 0
    while i < len(tokens):
        if tokens[i].type == "NUMBER":
            pass1.append(NumNode(tokens[i].value))
            i += 1
        elif tokens[i].type == "STAR":
            left = pass1.pop()
            right = NumNode(tokens[i+1].value)
            pass1.append(BinOptNode('*', left, right))
            i += 2
        elif tokens[i].type == "SLASH":
            left = pass1.pop()
            right = NumNode(tokens[i+1].value)
            pass1.append(BinOptNode('/', left, right))
            i += 2
        else:
            pass1.append(tokens[i])  # Keep + and -
            i += 1
    
    # Pass 2: Handle + and -
    pass2 = []
    i = 0
    while i < len(pass1):
        if isinstance(pass1[i], (NumNode, BinOptNode)):
            pass2.append(pass1[i])
            i += 1
        elif pass1[i].type == "PLUS":
            left = pass2.pop()
            right = pass1[i+1]
            pass2.append(BinOptNode('+', left, right))
            i += 2
        elif pass1[i].type == "MINUS":
            left = pass2.pop()
            right = pass1[i+1]
            pass2.append(BinOptNode('-', left, right))
            i += 2
        else:
            i += 1
    
    return pass2[0]
                                
def evaluate(node):
    if isinstance(node, NumNode):
        return node.value
    elif isinstance(node, BinOptNode):
        left = evaluate(node.left)   # Recursively evaluate left side
        right = evaluate(node.right) # Recursively evaluate right side
        
        if node.value == '+':
            return left + right
        elif node.value == '-':
            return left - right
        elif node.value == '*':
            return left * right
        elif node.value == '/':
            return left / right
        

def evol(code):
    code = tokenize(code)
    code = ast_parse(code)
    code = evaluate(code)
    return code



def readFile(filename):
    with open(args.filename, "r") as f:
        script = f.read()
    return script
        

def math(expression):
    return(eval(expression))



env = {}

def alloc(name, type, value):
    env[name] = type(value)


def get(name):
    return env[name]

lines = readFile(args.filename).splitlines()
for line in lines:
    if line.strip():
        print(ast_parse(tokenize(line)))
        print(env)