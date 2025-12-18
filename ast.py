import re, decimal
from functions import function_list, constants

class Parse:
    def __init__(self, expression):
        self.tokens = self.tokenize(expression)
        self.i = 0
        self.ast = self.comparison()

    def tokenize(self, expression):
        ''' Tokenize the input expression into numbers, operators, and parentheses '''
        return re.findall(r'\d+\.\d+|\d+|[a-zA-Z]+|!==|===|<==|>==|<=|>=|==|!=|<<|>>|//|\*\*|[<>]|[+*/()!$£%\-\^\.&\|~]', expression)

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
    
    def comparison(self):
        return self._exp(('<', '<=', '>', '>=', '==', '!=', '===', '!==', '<==', '>=='), self.bitor)

    def bitor(self):
        ''' Parse bitwise OR '''
        return self._exp(('|',), self.bitxor)

    def bitxor(self):
        ''' Parse bitwise XOR '''
        return self._exp(('xor', 'XOR'), self.bitand)

    def bitand(self):
        ''' Parse bitwise AND '''
        return self._exp(('&',), self.shift)

    def shift(self):
        ''' Parse bitwise shifts '''
        return self._exp(('<<', '>>'), self.expr)

    def expr(self):
        ''' Parse add and subtract '''
        return self._exp(('+', '-'), self.term)

    def term(self):
        ''' Parse multiply and divide '''
        return self._exp(('*', '/', '//', '%', '.'), self.percomb)

    def percomb(self):
        ''' Parse permutations and combinations '''
        return self._exp(('P', 'C'), self.power)

    def power(self):
        ''' Raise to the power '''
        node = self.prefix()
        if self.peek() in ('^', '**'):
            self.eat()
            node = ('symbol', '^', node, self.power())
        return node

    def prefix(self):
        if self.peek() == '~':
            self.eat()
            return ('unary', '~', self.prefix())
        return self.postfix()

    def postfix(self):
        ''' Parse postfix operators like factorial '''
        node = self.factor()
        while self.peek() in ('!','$', '£'):
            op = self.eat()
            node = ('postfix', op, node)
        return node

    def factor(self):
        ''' Parse numbers and parenthesized '''
        t = self.eat()
        if t == '(':
            n = self.comparison()
            self.eat()
            return n
        
        # Skip symbol
        if t in ['£', '$']:
            return self.factor()

        # check for function
        if t in function_list:
            self.eat()
            arg = self.comparison()
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

        if node[0] == 'postfix':
            _, op, inner = node
            val = self.evaluate(inner)
            if op in ('$', '£'):
                return val
            if op == '!':
                return function_list['factorial'](val)

        _, op, left, right = node
        a = self.evaluate(left)
        b = self.evaluate(right)

        # Arithmetic operators
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        elif op == '^':
            return a ** b
        elif op == '//':
            return a // b
        elif op == '%':
            return a % b
        elif op == '.':
            return a * b
        
        # Permutation and Combination
        elif op == 'P':
            return function_list['perm'](a, b)
        elif op == 'C':
            return function_list['comb'](a, b)
        
        # bitwise operators
        elif op == '&':
            return a & b
        elif op == '|':
            return a | b
        elif op == 'xor':
            return a ^ b
        elif op == '<<':
            return a << b
        elif op == '>>':
            return a >> b
        
        # Comparison operators
        elif op == '<':
            return a < b
        elif op == '<=':
            return a <= b
        elif op == '>':
            return a > b
        elif op == '>=':
            return a >= b
        elif op == '==':
            return a == b
        elif op == '!=':
            return a != b
        elif op == '===':
            return type(a) is type(b) and a == b
        elif op == '!==':
            return not (type(a) is type(b) and a == b)
        elif op == '<==':
            return type(a) is type(b) and a <= b
        elif op == '>==':
            return type(a) is type(b) and a >= b

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
