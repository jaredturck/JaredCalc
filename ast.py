import re, math

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
    
    def _const(self, t):
        ''' Check for mathematical constants '''
        if t == 'pi':
            return ('num', math.pi)
        if t == 'e':
            return ('num', math.e)
        if t == 'tau':
            return ('num', math.tau)
        if t == 'inf':
            return ('num', math.inf)
        if t == 'nan':
            return ('num', math.nan)
    
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
        
        # check for constant
        v = self._const(t)
        if v:
            return v
        
        # must be a number
        if '.' in t:
            return ('num', float(t))
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

if __name__ == '__main__':
    while True:
        expression = input('> ')
        t = Parse(expression)
        print(t.ast)
        print(t)
