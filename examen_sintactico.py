import ply.yacc as yacc
from examen_lexer import tokens


dicc = dict()

def p_cuerpo(p):   
    '''cuerpo : sentencia ';' '''
    p[0] = {p[1]}


def p_sentencia(p):
    '''sentencia : asignacion 
                | modificacion
                | retorno
                | eliminacion '''
    p[0] = p[1]  

def p_asignacion(p):
    '''asignacion : ID ASSIGN LCBRACKET objeto RCBRACKET '''
    
    try:
        p[0] = p[4]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

# def p_expresion(p):
#     '''expresion : params '''
#     p[0] = p[1]

def p_modificacion_index(p):
    '''asignacion : ID index ASSIGN dato '''
    try:
        p[0] = dicc[p[1]]
        dicc[p[1]] = p[3]
        p[0] = dicc[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_modificacion(p):
    '''modificacion : ID '.' ID  ASSIGN dato '''
    try:
        p[0] = dicc[p[3]]
        dicc[p[3]] = p[5]
        p[0] = dicc[p[3]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_retorno(p):
    '''retorno : ID '.' ID'''
    try:
        print(dicc[p[1]])
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0
def p_eliminacion(p):
    '''eliminacion : DELETE ID '.' ID'''
    try:
        del dicc[str(p[2])]
    except LookupError:
        print("Undefined name '%s'" % p[4])
        p[0] = 0

def p_objeto(p):
    '''objeto : ID ':' dato '''
    print('Objeto:',p)
    p[0] = p[3]
   


def p_index(p):
    '''index : ID LSBRACKET STRING RSBRACKET'''
    p[0] = p[3]

def p_dato(p): 
    '''dato : INT
            | FLOAT
            | BYTE
            | SHORT
            | DOUBLE
            | ID
            | LONG
            | CHAR
            | BOOLEAN
            | STRING'''
    p[0] = p[1]




# def p_params(p):
#     '''params : objeto ',' objeto
#             | objeto'''


# def p_args(p):
#     '''args : valor'''
#     p[0] = p[1]

# def p_args2(p):
#     '''args : args ',' args'''

# def p_valor_id(p):
#     '''valor : ID'''
#     p[0] = dicc[p[1]]

# def p_valor(p):
#     '''valor : number
#             | STRING'''
#     p[0] = p[1]

# def p_valor_bool(p):
#     '''valor : TRUE
#             | FALSE'''
#     if p[1] == 'true':
#         p[0] = True
#     else:
#         p[0] = False





# def p_asignacion_declarando(p):
#     '''asignacion : ID ASSIGN expresion '''
#     dicc[p[1]] = p[3]
#     p[0] = dicc[p[1]]
#     print(p[0])


# def p_declaracion(p):
#     '''declaracion : declarador ID '''
#     dicc[p[2]] = ""



# def p_exresion(p):
#     '''expresion : LPAREN expresion RPAREN'''

# def p_expesion(p):
#     '''expresion : valor '''
#     p[0] = p[1]



# def p_number(p):   
#     '''number : INTV
#             | FLOATV '''
#     p[0] = p[1]

    # Error rule for syntax errors


def p_error(p):
    print("Syntax error in input!")
    # Build the parser


parser = yacc.yacc()



print("\n\nSintactico")

while True:
    try:
        print()
        print(dicc)
        s = input('>>> ')
    except EOFError:
        break
    #if not s: continue
    result = parser.parse(s)
    print(result)