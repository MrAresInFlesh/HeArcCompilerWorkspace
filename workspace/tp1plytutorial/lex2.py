import ply.lex as lex

tokens = (
    'NUMBER',
    'ADD_OP',
    'MUL_OP'
)


def t_ADD_OP(t):
    r'\+|-'
    return t


def t_MUL_OP(t):
    r'\*|/'
    return t


def t_NUMBER(t):
    r'[+-]?([0-9]*[.])?[0-9]+'
    t.value = float(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s' % t.value[0]")
    t.lexer.skip(1)


lex.lex()

if __name__ == "__main__":
    filename = "prog1.txt"
    prog = open(filename).read()

    lex.input(prog)

    while 1:
        tok = lex.token()
        if not tok: break
        print("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))
