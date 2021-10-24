import ply.yacc as yacc
from lex2 import tokens


def p_expression_num(p):
    'expression : NUMBER'
    p[0] = p[1]


def p_expression_op(p):
    """expression : expression ADD_OP expression
    | expression MUL_OP expression"""

    p[0] = operations[p[2]](p[1], p[3])


def p_error(p):
    print("syntax error in line %d" % p.lineno)
    yacc.errok()


operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y
}

precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP')
)

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    filename = "prog1.txt"
    prog = open(filename).read()
    result = yacc.parse(prog)
    print(result)

