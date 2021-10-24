"Essai d'un parser descendant recursif a la main..."

from ply import lex


tokens = ('identifier',)
literals = '()+'
t_identifier = r'\w+'


def t_error(t):
    print("Error: ", t)


lex.lex()


def parse(s):
    global LATok
    lex.input(s)
    LATok = lex.token()  # read the first token from lexical analyser
    print(LATok)
    result = input()  # start parsing
    print(s, " -> parsing:", result)


def token(t):  # verify if current token (sent from the lexical analyser) is t. Returns BOOL
    global LATok  # Look-Ahead Token
    print("LATok", LATok)
    if not LATok:  # case of end of tokens, we return an EOF
        return t == 'EOF'
    if LATok.type != t:  # case of inexpected token
        return False
    LATok = lex.token()  # case of expected token, we consume the current and go for the next token
    return True


def require(found):  # just sends an error in case of inexpected parsing
    if found:
        return True
    t_error("Error while parsing near token %s!" % LATok.value)


def input():
    return expression() and require(token('EOF'))


def expression():
    return term() and require(rest_expression())


def term():
    return token('identifier') or parenth_expr()


def parenth_expr():
    return token('(') and require(expression()) and require(token(')'))


def rest_expression():
    return (token('+') and require(expression())) or True


if __name__ == '__main__':
    parse('3+(2+2)+')
