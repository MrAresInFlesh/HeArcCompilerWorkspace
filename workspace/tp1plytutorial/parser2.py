import ply.yacc as yacc
from lex3 import tokens

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y
}


def p_expression_num(p):
    """expression : NUMBER"""
    p[0] = p[1]


def p_expression_op(p):
    """expression : expression ADD_OP expression
    | expression MUL_OP expression"""
    p[0] = operations[p[2]](p[1], p[3])


def p_expression_paren(p):
    """expression : '(' expression ')' """
    p[0] = p[2]


def p_minus(p):
    """expression : ADD_OP expression %prec UNARY_MINUS"""
    p[0] = operations[p[1]](0, p[2])


def p_error(p):
    print("syntax error in line %d" % p.lineno)
    yacc.errok()


precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('right', 'UNARY_MINUS'),
)

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    filename = "prog2.txt"
    prog = open(filename).read()
    result = yacc.parse(prog)
    print(result)
