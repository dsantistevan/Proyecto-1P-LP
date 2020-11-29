#David Santistevan - Kotlin 1
from ply import lex

reservadas={"true" : "TRUE", 'false':'FALSE','int':'INT', 'byte':'BYTE', 'float':'FLOAT', 'short':'SHORT',
            'long':'LONG', 'double':'DOUBLE', 'boolean':'BOOLEAN', 'char':'CHAR','in':'IN','delete':'DELETE'}

tokens = (
    'ID',
    'FLOATV',
    'INTV',
    'LPAREN',
    'RPAREN',
    'LSBRACKET',
    'RSBRACKET',
    'LCBRACKET',
    'RCBRACKET',
    'ASSIGN',
    'STRING',
) + tuple(reservadas.values())
# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'\='
t_LCBRACKET = r'\{'
t_RCBRACKET = r'\}'
t_LSBRACKET = r'\['
t_RSBRACKET = r'\]'

literals = [';', ':', ".", ",",'\\']

def t_STRING(t):
    r'((\"[^(\")]*\")|(\'[^(\')]*\'))'
    t.type = reservadas.get(t.value, 'STRING')
    return t

def t_ID(t):
    r'[a-zA-Z\_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'ID')
    return t


def t_FLOATV(t):
    r'(-|\+)?\d*(\.\d+)'
    t.value = float(t.value)
    return t

def t_INTV(t):
    r'(-|\+)?\d+'
    t.value = int(t.value)
    return t

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

lexer = lex.lex()

# def analizar(data):
#     lexer.input(data)
# # Tokenize
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break  # No more input
#         print(tok)


# while True:
#     linea = input(">>> ")
#     analizar(linea)
