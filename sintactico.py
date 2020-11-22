import ply.yacc as yacc
from lexicoSantistevan import tokens
import time


def p_cuerpo(p):
    '''cuerpo : cuerpo sentencia
		| sentencia'''

def p_sentencia(p):
    '''sentencia : asignacion
                | expresion
                | estructuraControl
                | bucles '''

def p_instrucciones(p):
    '''instrucciones : LCBRACKET cuerpo RCBRACKET
                | cuerpo '''

#estructuraControls
def p_estructuraControlIf(p):
    '''estructuraControl : IF LPAREN expresion RPAREN instrucciones '''

def p_estructuraControlElse(p):
    '''estructuraControl : ELSE instrucciones '''

def p_bucles(p):
    '''bucles : while instrucciones
                | for instrucciones '''


#while
def p_while(p):
    '''while : WHILE LPAREN expresion RPAREN '''

#for
def p_for(p):
    '''for : FOR LPAREN ID IN ID RPAREN '''


def p_valor(p):
    '''valor : number
            | ID
            | STRING'''


def p_valor_negado(p):
    '''valor : NOT valor '''
    p[0] = (not p[2])


def p_asignacion(p):
    '''asignacion : ID ASSIGN expresion ';' '''




def p_expesion(p):
    '''expresion : valor '''


def p_expresion_matematica(t):
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

def p_expresion_logica(t):
    'expresion : expresion operadoresLog expresion '
    if t[2] == '||':
        t[0] = t[1] or t[3]
    elif t[2] == '&&':
        t[0] = t[1] and t[3]
    elif t[2] == '==':
        t[0] = t[1] == t[3]
    elif t[2] == '!=':
        t[0] = t[1] != t[3]

def p_operadoresLog(p):
    '''operadoresLog :  OR
                    | AND
                    | EQUALS
                    | NOTEQUALS '''


def p_operadoresMat(p):
    '''operadoresMat : MINUS
                    | PLUS
                    | TIMES
                    | DIVIDE
                    | MODULE '''





def p_number(p):
    '''number : INTV
            | FLOATV '''



    # Error rule for syntax errors


def p_error(p):
    print("Syntax error in input!")
    print("ASD")
    # Build the parser


parser = yacc.yacc()

def analizar2(data):
    result = parser.parse(data)
# Tokenize
    print(result)


def analizarArchivo2(nombre= "codigoTodos.txt"):
    f = open(nombre, "r")
    parser.parse(f.read())
    f.close()


print("\n\nSintactico")

#time.sleep(2)

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