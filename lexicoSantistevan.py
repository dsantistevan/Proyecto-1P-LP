#David Santistevan - Kotlin 1

from ply import lex

reservadas={'var':'VAR','while':'WHILE','if':'IF','else':'ELSE','for':'FOR', "true" : "TRUE", 'false':'FALSE',
            'return': 'RETURN', 'null':'NULL', 'int':'INT', 'byte':'BYTE', 'float':'FLOAT', 'short':'SHORT',
            'long':'LONG', 'double':'DOUBLE', 'boolean':'BOOLEAN', 'char':'CHAR', 'fun':'FUNCTION'}

tokens = (
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULE',
    'LPAREN',
    'RPAREN',
    'LSBRACKET',
    'RSBRACKET',
    'LCBRACKET',
    'RCBRACKET',
    'ASSIGN',
    'GREATER',
    'LOWER',
    'NOT',
    'AND',
    'OR',
    'STRING'
) + tuple(reservadas.values())
# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULE= r'\%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'\='
t_GREATER = r'\>'
t_LOWER = r'\<'
t_LCBRACKET = r'\{'
t_RCBRACKET = r'\}'
t_NOT = r'\!'
t_OR = r'\|\|'
t_AND = r'\&\&'
t_LSBRACKET = r'\['
t_RSBRACKET = r'\]'

literals = [';', ':']

def t_STRING(t):
    r'(\"[\w\W]\"|\'[\w\W]\')'
    return t

def t_ID(t):
    r'[a-zA-Z\_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'ID')
    return t


t_NUMBER  =r'(-|\+)?\d+(\.\d*)?'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'
t_ignore_COMMENT1 = r'\/\/[\S\ ]*$'
t_ignore_COMMENT2 = r'\/\*[^(\*\/)]* \*\/'


# Error handling rule
def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)



# Build the lexer
lexer = lex.lex()
# Test it out
f = open("codigoSantistevan.txt", "r")

# Give the lexer some input

def analizar(data):
    lexer.input(data)
# Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

for linea in f:
    print(">>" + linea)
    analizar(linea)
    if len(linea) ==0:
        break