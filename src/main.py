'''
import re

from .AST import string as AST_string

def run(string: str) -> str:
    print_re = re.compile(r'''^\s*print\s*,\s*(.*?)\s*$''')
    result = print_re.findall(string)
    if result:
        return AST_string(result[0], 0)[0]
    raise ValueError("not the deal that we want")
'''

from rply import LexerGenerator
 
lg = LexerGenerator()
 
lg.add('NUMBER', r'\d+')
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')
lg.add('MUL', r'\*')
lg.add('DIV', r'/')
lg.add('OPEN_PARENS', r'\(')
lg.add('CLOSE_PARENS', r'\)')
lg.add('PRINT',r'print')
lg.add('STRING',r'"\w"')
 
lg.ignore('\s+')
 
lexer = lg.build()
 
from rply.token import BaseBox
 
class Number(BaseBox):
    def __init__(self, value):
        self.value = value
 
    def eval(self):
        return self.value
        
class String(BaseBox):
    def __init__(self, value):
        self.value = value
 
    def eval(self):
        return self.value
 
class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right
 
class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()
 
class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()
 
class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()
 
class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()
 
class Print(BinaryOp):
	def eval(self):
		return self.right.eval()
 
from rply import ParserGenerator
 
pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['NUMBER','STRING', 'OPEN_PARENS', 'CLOSE_PARENS',
     'PLUS', 'MINUS', 'MUL', 'DIV','PRINT'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV']),
        ('right',['PRINT'])
    ]
)
 
@pg.production('expression : NUMBER')
def expression_number(p):
    # p is a list of the pieces matched by the right hand side of the
    # rule
    return Number(int(p[0].getstr()))

@pg.production('expression : STRING')
def expression_number(p):
    # p is a list of the pieces matched by the right hand side of the
    # rule
    return String(p[0].getstr())
   
@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
    return p[1]
 
@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MINUS expression')
@pg.production('expression : expression MUL expression')
@pg.production('expression : expression DIV expression')
def expression_binop(p):
    left = p[0]
    right = p[2]
    if p[1].gettokentype() == 'PLUS':
        return Add(left, right)
    elif p[1].gettokentype() == 'MINUS':
        return Sub(left, right)
    elif p[1].gettokentype() == 'MUL':
        return Mul(left, right)
    elif p[1].gettokentype() == 'DIV':
        return Div(left, right)
    else:
        raise AssertionError('Oops, this should not be possible!')
 
@pg.production('expression : PRINT expression')
def expression_func(p):
	right = p[1]
	if p[0].gettokentype() == 'PRINT':
		return Print(None, right)
 
parser = pg.build()
 
@pg.error
def error_handler(token):
    raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())
    

while(True):
	try:
		print(parser.parse(lexer.lex(input(">>>"))).eval())
	except Exception as e:
			print(e)
