# Dylan Escala Kotlin 1
import ply.lex as lex
reservadas={'var':'VAR','while':'WHILE','if':'IF','else':'ELSE','for':'FOR'}
tokens = [
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS','EQUALSBOOL',
    'LPAREN','RPAREN','ignore','var','nombrevar','var2',
    'MENE','MAYE','MAY','MEN','DIF','LLAVEA','LLAVEC','CORCHEA','CORCHEC'
    ]

# Tokens
t_EQUALS  = r'='
#ARITMETICOS
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD  = r'%'
#COMPARACION
t_EQUALSBOOL  = r'=='
t_MENE=r'<='
t_MAYE=r'>='
t_MAY=r'>'
t_MEN=r'<'
t_DIF=r'!='
#AGRUPACION
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LLAVEA=r'{'
t_LLAVEC=r'}'
t_CORCHEA=r'['
t_CORCHEC=r']'
#OTROS
t_NUMBER = r'\d+'
t_ignore = " \t"
#t_while=r"while"
#t_nombrevar=r"[a-zA-Z][a-zA-Z0-9_]*"
t_var2=r':'
#t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*''
def t_nombrevar(t):
    r"[a-zA-Z][a-zA-Z0-9_]*"
    t.type=reservadas.get(t.value,'nombrevar')
    return t

    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
def t_newline(t):
    r'\n+'
    #t.lexer.lineno += t.value.count("\n")


archivo = open("archivo.txt")
for linea in archivo:
    print(">>"+linea)
    #analizar(linea)
    lexer = lex.lex()
    lexer.input(linea)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

