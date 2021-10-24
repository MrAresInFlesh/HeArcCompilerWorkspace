from ply import lex
import sys


# _____________________________________________________________________________________#
# FUNCTIONS DECORATOR

def debug(f):
    def inner(*args):
        print("%-5s%s %s: %s" %
              (LATok.value if LATok else 'EOF', debug.indent, f.__name__, ",".join(args) if args else ''))
        debug.indent += ' | '
        result = f(*args)
        debug.indent = debug.indent[:-3]
        if not result:
            print("%-5s%s** Failed!" % (LATok.value if LATok else 'EOF', debug.indent))
        return result

    return inner


def t_error(t):
    print("err")


debug.indent = ''
tokens = ('identifier',)
literals = '()+*'
t_identifier = r'\w+|\*'

# _____________________________________________________________________________________#


lex.lex()


def parse(s):
    global LATok
    print("** parsing: ", s)
    lex.input(s)
    LATok = lex.token()  # read the first token from lexical analyser
    result = input()  # start parsing
    print("** result: ", result)


@debug
def token(t):
    global LATok
    if not LATok:
        return t == 'EOF'  # case of the end of tokens, we return an EOF
    if LATok.type != t:
        return False  # case of inexpected found token
    LATok = lex.token()  # case of correctly expected token
    return True


def require(found):
    if found:
        return True
    print("Error while parsing near token %s!" % LATok.value if LATok else 'EOF')
    sys.exit(0)


@debug
def input():
    return expression() and require(token('EOF'))


@debug
def expression():
    return term() and require(rest_expression())


@debug
def term():
    return token('identifier') or parenth_expr()


@debug
def parenth_expr():
    return token('(') and require(expression()) and require(token(')'))


@debug
def rest_expression():
    return (token('+') and require(expression())) or True


@debug
def mul_expression():
    return (token('*') and require(expression())) or True


if __name__ == '__main__':
    parse('12+3+3')
