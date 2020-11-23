import ply.yacc as yacc
from lexicoSantistevan import tokens


names = {}

def p_cuerpo(p):    #David Santistevan
    '''cuerpo : sentencia  '''
    p[0] = [p[1]]


def p_cuerpoR(p):   #David Santistevan
    '''cuerpo : sentencia cuerpo'''
    p[0] = [p[1]] + p[2]

def p_cuerpo_funcion(p):    #David Santistevan
    '''cuerpo : function cuerpo'''
    p[0] = [p[1]] + p[2]


def p_sentencia(p): #Dylan Escala
    '''sentencia : asignacion ';'
                | expresion
                | estructuraControl
                | bucles
                | llamada ';' '''
    p[0] = p[1]

def p_instrucciones(p): #David Santistevan
    '''instrucciones : LCBRACKET cuerpo RCBRACKET
                | sentencia '''

def p_instrucciones_funcion(p): #David Santistevan
    '''instruccionesF : LCBRACKET cuerpo retorno RCBRACKET'''

def p_retorno(p):   #David Santistevan
    '''retorno : RETURN valor ';' '''


#estructuraControls - Dylan Escala
def p_estructuraControlIf(p):
    '''estructuraControl : IF LPAREN expresion RPAREN instrucciones '''

def p_estructuraControlElse(p):
    '''estructuraControl : ELSE instrucciones '''

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


def p_llamada_funcion(p):
    '''llamada : ID LPAREN args RPAREN '''


def p_llamada_funcion_sin_params(p):
    '''llamada : ID LPAREN RPAREN '''


def p_index(p): #David Santistevan
    '''function : ID LSBRACKET valor RSBRACKET'''


def p_dato(p):  #David Santistevan
    '''dato : INT
            | FLOAT
            | BYTE
            | SHORT
            | DOUBLE
            | ID
            | LONG
            | CHAR
            | BOOLEAN'''


def p_params(p):  #David Santistevan
    '''params : ID ':' dato '''


def p_params2(p): #David Santistevan
    '''params : params ',' params'''


def p_args(p):
    '''args : valor'''
    p[0] = p[1]

def p_args2(p):
    '''args : args ',' args'''

def p_valor(p): #David Santistevan
    '''valor : number
            | ID
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
    names[p[1]] = p[3]
    p[0] = names[p[1]]


def p_declaracion1(p): #David Santistevan
    '''declarador : VAR ID'''
    names[p[1]] = None


def p_declaracion2(p): #David Santistevan
    '''declarador : VAL ID'''
    names[p[1]] = None


def p_exresion(p): #David Santistevan
    '''expresion : LPAREN expresion RPAREN'''

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
            raise ZeroDivisionError('number division by 0')
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

def p_operadores_log(p):    #Dylan Escala
    '''operadoresLog :  OR
                    | AND
                    | EQUALS
                    | NOTEQUALS
                    | GREATER
                    | LOWER
                    | GREATER ASSIGN
                    | LOWER ASSIGN'''
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



    # Error rule for syntax errors


def p_error(p):
    print("Syntax error in input!")
    # Build the parser


parser = yacc.yacc()

def analizar2(data):
    result = parser.parse(data)
# Tokenize
    print(result)


def analizarArchivo2(nombre= "codigoTodos.txt"):
    f = open(nombre, "r")
    linea = f.readline()

    while linea != "":
        if linea.find("/*") != -1:
            while linea.find("*/") == -1:
                linea+=f.readline()
        print(">>" + linea)
        analizar2(linea)
        linea= f.readline()
    f.close()


print("\n\nSintactico")


#analizarArchivo2()

#print(parser.parse("""for(i in Lista){
#    i = 2
#}"""))

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    #if not s: continue
    result = parser.parse(s)
    print(result)