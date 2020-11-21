#David Santistevan - Kotlin 1
import ply.yacc as yacc
from ply import lex

reservadas={'var':'VAR','while':'WHILE','if':'IF','else':'ELSE','for':'FOR', "true" : "TRUE", 'false':'FALSE',
            'return': 'RETURN', 'null':'NULL', 'int':'INT', 'byte':'BYTE', 'float':'FLOAT', 'short':'SHORT',
            'long':'LONG', 'double':'DOUBLE', 'boolean':'BOOLEAN', 'char':'CHAR', 'fun':'FUNCTION', 'val':'VAL'}

tokens = (
    'ID',
    'FLOATV',
    'INTV',
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
    'EQUALS',
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
t_EQUALS = r'\=\='
t_GREATER = r'\>'
t_LOWER = r'\<'
t_LCBRACKET = r'\{'
t_RCBRACKET = r'\}'
t_NOT = r'\!'
t_OR = r'\|\|'
t_AND = r'\&\&'
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
    r'(-|\+)?\d*(\.\d*)'
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
# Test it out

# Give the lexer some input

def analizar(data):
    lexer.input(data)
# Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


def analizarArchivo(nombre= "codigoTodos.txt"):
    f = open(nombre, "r")
    linea = f.readline()
    while linea != "":
        if linea.find("/*") != -1:
            while linea.find("*/") == -1:
                linea+=f.readline()
        print(">>" + linea)
        analizar(linea)
        linea= f.readline()


    f.close()

analizarArchivo()
#analizarArchivo('codigoJimenez.txt')

