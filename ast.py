import re, decimal
from functions import function_list, constants

class Parse:
    def __init__(self, expression):
        self.tokens = self.tokenize(expression)
        self.i = 0
        self.ast = self.expr()
    
    def tokenize(self, expression):
        ''' Tokenize the input expression into numbers, operators, and parentheses '''
        return re.findall(r'\d+\.\d+|\d+|[a-zA-Z]+|[+*/()-]', expression)
    
    def peek(self):
        ''' Look at the next token without consuming it '''
        return self.tokens[self.i] if self.i < len(self.tokens) else None
    
    def eat(self):
        ''' Consume and return the next token '''
        t = self.peek()
        self.i += 1
        return t
    
    def _exp(self, symbols, func):
        ''' Generic expression parser for left-associative binary operations '''
        node = func()
        while self.peek() in symbols:
            op = self.eat()
            node = ('symbol', op, node, func())
        return node
    
    def expr(self):
        ''' Parse add and subtract '''
        return self._exp(('+', '-'), self.term)
    
    def term(self):
        ''' Parse multiply and divide '''
        return self._exp(('*', '/'), self.factor)
    
    def factor(self):
        ''' Parse numbers and parenthesized '''
        t = self.eat()
        if t == '(':
            n = self.expr()
            self.eat()
            return n
        
        # check for function
        if t in function_list:
            self.eat()
            arg = self.expr()
            self.eat()
            return ('function', t, arg)
        
        # check for constant
        if t in constants:
            return ('num', constants[t])
        
        # must be a number
        if '.' in t:
            return ('num', decimal.Decimal(t))
        return ('num', int(t))
    
    def evaluate(self, node=None):
        ''' Evaluate the AST recursively '''
        if not node:
            node = self.ast
        if node[0] == 'num':
            return node[1]
        if node[0] == 'function':
            _, name, arg = node
            val = self.evaluate(arg)
            return function_list[name](val)
        
        _, op, left, right = node
        a = self.evaluate(left)
        b = self.evaluate(right)

        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
    
    def __str__(self):
        v = self.evaluate()
        if isinstance(v, float):
            return format(decimal.Decimal(v).normalize(), "f")
        if isinstance(v, decimal.Decimal):
            return format(v.normalize(), "f")
        return str(v)

if __name__ == '__main__':
    while True:
        expression = input('> ')
        t = Parse(expression)
        print(t.ast)
        print(t)
