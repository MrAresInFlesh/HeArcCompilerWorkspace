import ply.yacc as yacc
import AST
import os
from lex4 import tokens

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y
}


def p_programme_statement(p):
    """programme : statement"""
    p[0] = AST.ProgramNode(p[1])


def p_programme_recursive(p):
    """programme : statement ';' programme"""
    p[0] = AST.ProgramNode([p[1]] + p[3].children)


def p_statement(p):
    """statement : assignation
    | expression"""
    p[0] = p[1]


def p_expression_op(p):
    """expression : expression ADD_OP expression
    | expression MUL_OP expression"""
    p[0] = AST.OpNode(p[2], [p[1], p[3]])


def p_expression_num(p):
    """expression : NUMBER
    | IDENTIFIER"""
    p[0] = AST.TokenNode(p[1])


def p_expression_paren(p):
    """expression : '(' expression ')'"""
    p[0] = p[2]


def p_minus(p):
    """expression : ADD_OP expression %prec UNARY_MINUS"""
    p[0] = AST.OpNode(p[1], [p[2]])


def p_assignation(p):
    """assignation : IDENTIFIER '=' expression"""
    p[0] = AST.AssignNode([AST.TokenNode(p[1]), p[3]])


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

    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
    graph = result.makegraphicaltree()
    name = os.path.splitext(filename)[0] + '-ast.pdf'
    graph.write_pdf(name)
    print("wrote ast to", name)
