import re

class Parse:
    def __init__(self, expression):
        self.tokens = re.findall(r'\d+|[+*/()-]', expression)
        self.i = 0
        self.ast = self.expr()
    
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
        return ('num', int(t))
    
    def evaulate(self, node=None):
        ''' Evaluate the AST recursively '''
        if not node:
            node = self.ast
        if node[0] == 'num':
            return node[1]
        
        _, op, left, right = node
        a = self.evaulate(left)
        b = self.evaulate(right)

        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
    
    def __str__(self):
        return str(self.evaulate())

t = Parse('3 * (4 + 5 + (6 / 7))')
print(t.ast)
print(t)
