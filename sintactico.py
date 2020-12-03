import ply.yacc as yacc
from lexicoSantistevan import tokens


names = {}

def p_cuerpo(p):    #David Santistevan
    '''cuerpo : sentencia  '''
    p[0] = [p[1]]

def p_cuerpo_funcion_sola(p):    #David Santistevan
    '''cuerpo : function  '''
    p[0] = [p[1]]

def p_cuerpoR(p):   #David Santistevan
    '''cuerpo : sentencia cuerpo'''
    p[0] = [p[1]] + p[2]

def p_cuerpo_funcion(p):    #David Santistevan
    '''cuerpo : function cuerpo'''
    p[0] = [p[1]] + p[2]


def p_sentencia(p): #Dylan Escala # Fixed by Carlos Jimenez
    '''sentencia : asignacion 
                | estructuraControl
                | bucles
                | llamada
                | declaracion '''
    p[0] = p[1]

def p_instrucciones(p): #David Santistevan
    '''instrucciones : LCBRACKET cuerpo RCBRACKET
                | sentencia '''

def p_instrucciones_funcion(p): #David Santistevan
    '''instruccionesF : LCBRACKET cuerpo retorno RCBRACKET'''

def p_instrucciones_funcion_retorno(p): #David Santistevan
    '''instruccionesF : LCBRACKET retorno RCBRACKET'''


def p_instrucciones_funcion_dato(p): #David Santistevan
    '''instruccionesF : ':' dato LCBRACKET cuerpo retorno RCBRACKET'''


def p_instrucciones_funcion_retorno_dato(p): #David Santistevan
    '''instruccionesF : ':' dato LCBRACKET retorno RCBRACKET'''

def p_retorno(p):   #David Santistevan # Fixed by Carlos Jimenez
    '''retorno : RETURN expresion '''


#estructuraControls - Dylan Escala
def p_estructuraControlIf(p):
    '''estructuraControl : IF LPAREN expresion RPAREN instrucciones '''
#Dylan Escala
def p_estructuraControlElse(p):
    '''estructuraControl : ELSE instrucciones '''
#Dylan Escala
def p_bucles(p):
    '''bucles : while instrucciones
                | for instrucciones '''


#while - Dylan Escala
def p_while(p):
    '''while : WHILE LPAREN expresion RPAREN '''

#for - Dylan Escala
def p_for(p):
    '''for : FOR LPAREN ID IN ID RPAREN '''


#function
def p_function(p):  #David Santistevan
    '''function : FUNCTION ID LPAREN params RPAREN instruccionesF'''

def p_function_sin_params(p):  #David Santistevan
    '''function : FUNCTION ID LPAREN RPAREN instruccionesF'''

def p_print(p):
    '''llamada : PRINTLN LPAREN expresion RPAREN'''
    print(p[3])
    p[0] = p[3]

def p_llamada_funcion(p):
    '''llamada : ID LPAREN args RPAREN '''


def p_llamada_funcion_sin_params(p):
    '''llamada : ID LPAREN RPAREN '''


def p_llamada_objeto(p):
    '''llamada : ID '.' ID LPAREN args RPAREN'''

def p_llamada_objeto_sin_params(p):
    '''llamada : ID '.' ID LPAREN RPAREN'''


def p_index(p): #David Santistevan
    '''function : ID LSBRACKET expresion RSBRACKET'''
    p[0] = names[p[1]][p[3]]


def p_dato(p):  #David Santistevan
    '''dato : INT
            | FLOAT
            | BYTE
            | SHORT
            | DOUBLE
            | ID
            | LONG
            | CHAR
            | BOOLEAN
            | LIST
            | MUTABLELIST'''


def p_params(p):  #David Santistevan
    '''params : ID ':' dato '''


def p_params2(p): #David Santistevan
    '''params : params ',' params'''


def p_args(p):
    '''args : expresion'''
    p[0] = [p[1]]

def p_args2(p):
    '''args : args ',' args'''
    p[1].extend(p[2])
    p[0] = p[1]

def p_valor_id(p):
    '''valor : ID'''
    p[0] = names[p[1]]

def p_valor(p): #David Santistevan
    '''valor : number
            | STRING'''
    p[0] = p[1]

def p_valor_bool(p): #David Santistevan
    '''valor : TRUE
            | FALSE'''
    if p[1] == 'true':
        p[0] = True
    else:
        p[0] = False


def p_valor_null(p): #David Santistevan
    '''valor : NULL'''
    p[0] = None


def p_valor_negado(p): #David Santistevan
    '''valor : NOT valor '''
    p[0] = (not p[2])


def p_declarador(p): #David Santistevan
    '''declarador : VAR
                | VAL'''


def p_asignacion(p): #David Santistevan
    '''asignacion : ID ASSIGN expresion '''
    try:
        p[0] = names[p[1]]
        names[p[1]] = p[3]
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_asignacion_declarando(p): #David Santistevan
    '''asignacion : declarador ID ASSIGN expresion '''
    names[p[2]] = p[4]
    p[0] = names[p[2]]
    print(p[0])


def p_declaracion(p): #David Santistevan # Fixed by Carlos Jimenez
    '''declaracion : declarador ID '''
    names[p[2]] = ""


def p_creacion_lista(p):
    '''llamada : LISTOF LPAREN params RPAREN'''
    p[0] = tuple(p[3])


def p_creacion_set(p):
    '''llamada : SETOF LPAREN params RPAREN'''
    p[0] = set(p[3])

def p_creacion_lista_mutable(p):
    '''llamada : MUTABLELISTOF LPAREN params RPAREN'''
    p[0] = list(p[3])

def p_expresion_llamada(p):
    '''expresion : llamada'''
    p[0] = p[1]


def p_exresion(p): #David Santistevan
    '''expresion : LPAREN expresion RPAREN'''
    p[0] = p[2]

def p_expesion(p): #David Santistevan
    '''expresion : valor '''
    p[0] = p[1]


def p_expresion_matematica(t): #Dylan Escala
    'expresion : expresion operadoresMat expresion '
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        if t[3] != 0:
            t[0] = t[1] / t[3]
        else:
            print("Can't divide by 0")
            raise ZeroDivisionError('Number division by 0')
    elif t[2] == '%':
        t[0] = t[1] % t[3]

def p_expresion_logica(t): #Dylan Escala
    'expresion : expresion operadoresLog expresion '
    if t[2] == '||':
        t[0] = t[1] or t[3]
    elif t[2] == '&&':
        t[0] = t[1] and t[3]
    elif t[2] == '==':
        t[0] = t[1] == t[3]
    elif t[2] == '!=':
        t[0] = t[1] != t[3]
    elif t[2] =='>':
        t[0] = t[1] > t[3]
    elif t[2] =='>=':
        t[0] = t[1] >= t[3]
    elif t[2] =='<':
        t[0] = t[1] < t[3]
    elif t[2] =='<=':
        t[0] = t[1] <= t[3]

def p_operadores_log(p):    #Dylan Escala
    '''operadoresLog :  OR
                    | AND
                    | EQUALS
                    | NOTEQUALS
                    | GREATER
                    | LOWER
                    | GREATERE
                    | LOWERE'''
    p[0] = p[1]


def p_operadores_mat(p):    #Dylan Escala
    '''operadoresMat : MINUS
                    | PLUS
                    | TIMES
                    | DIVIDE
                    | MODULE '''
    p[0] = p[1]





def p_number(p):    #David Santistevan
    '''number : INTV
            | FLOATV '''
    p[0] = p[1]

<<<<<<< HEAD

# def p_list_length(p):
#     '''llamada : ID '.' LENGTH LPAREN RPAREN'''
#     l = names[p[1]]
#     if type(l) in (tuple, list):
#         p[0] = len(l)
#     else:
#         raise Exception("Variable not a list")
=======
def p_string_length(p):
    '''llamada : ID '.' LENGTH LPAREN RPAREN'''
    s = names[p[1]]
    if type(s) == str:
        p[0] = len(s)
    else:
        raise Exception("Variable not a String")


def p_string_equals(p):
    '''llamada : ID '.' EQUALSM LPAREN ID RPAREN'''
    s = names[p[1]]
    s2 = names[p[5]]
    if type(s) == str and type(s2) == str:
        p[0] = len(s)
    else:
        raise Exception("Variable not a String")


def p_string_equals2(p):
    '''llamada : ID '.' EQUALSM LPAREN STRING RPAREN'''
    s = names[p[1]]
    if type(s) == str:
        p[0] = s == p[5]
    else:
        raise Exception("Variable not a String")

def p_list_count(p):
    '''llamada : ID '.' COUNT LPAREN RPAREN'''
    l = names[p[1]]
    if type(l) in (tuple, list):
        p[0] = len(l)
    else:
        raise Exception("Variable not a List")
>>>>>>> 1da17990edf57a74b73d7f4a526b56715393e6a8

def p_list_first(p):
    '''llamada : ID '.' FIRST LPAREN RPAREN'''
    l = names[p[1]]
    if type(l) in (tuple, list):
        p[0] = l[0]
    else:
        raise Exception("Variable not a List")

def p_list_last(p):
    '''llamada : ID '.' LAST LPAREN RPAREN'''
    l = names[p[1]]
    if type(l) in (tuple, list):
        p[0] = l[-1]
    else:
        raise Exception("Variable not a List")

    # Error rule for syntax errors
def p_list_get(p):
    '''llamada : ID '.' GET LPAREN INTV RPAREN'''
    l = names[p[1]]
    if type(l) in (tuple, list):
        p[0] = l[p[5]]
    else:
        raise Exception("Variable not a List")

def p_list_get2(p):
    '''llamada : ID '.' GET LPAREN ID RPAREN'''
    l = names[p[1]]
    i = names[p[5]]
    if type(l) in (tuple, list) and type(i) == int and i>=0:
        p[0] = l[i]
    else:
        raise Exception("Variable not a List")


def p_error(p):
    print("Syntax error in input!")
    # Build the parser


parser = yacc.yacc()

def analizar2(data):
    result = parser.parse(data)
# Tokenize
    print(result)



def analizarArchivo2(nombre= "codigoSintacticoDavid.txt"):
    f = open(nombre, "r")
    texto = f.read()
    f.close()
    analizar2(texto)


def analizarArchivoJimenez(nombre= "codigoSintacticoJimenez.txt"):
    f = open(nombre, "r")
    texto = f.read()
    f.close()
    analizar2(texto)

# analizarArchivo2()
# analizarArchivoJimenez()

#print(parser.parse("""for(i in Lista){
#    i = 2
#}"""))

# while True:
#     try:
#         print()
#         print(names)
#         s = input('calc > ')
#     except EOFError:
#         break
#     #if not s: continue
#     result = parser.parse(s)
#     print(result)