import ply.yacc as yacc
from lexicoSantistevan import tokens
def p_cuerpo(p):
    '''cuerpo : asignacion
                | expresion
                | sentencia
                | bucles'''
#sentencias
def p_sentencia(p):
    '''sentencia : IF LPAREN expresion RPAREN '''

def p_sentenciaelse(p):
    '''sentencia : ELSE '''

def p_bucles(p):
    '''bucles : while
              | for'''
#while
def p_while(p):
    '''while : WHILE LPAREN expresion RPAREN '''

def p_for(p):
    '''for : FOR LPAREN ID IN ID RPAREN '''
#for
def p_asignacion(p):
    'asignacion : VAR ID ASSIGN expresion'

def p_expesion(p):
    '''expresion : valor'''

def p_expresion_matematica(p):
    'expresion : expresion operadoresMat expresion'

def p_expresion_logica(p):
    'expresion : expresion operadoresLog expresion'

def p_operadoresLog(p):
    '''operadoresLog : NOT
                    | OR
                    | AND
                    | EQUALS'''

def p_operadoresMat(p):
    '''operadoresMat : MINUS
                    | PLUS
                    | TIMES
                    | DIVIDE'''

def p_expression_plus(p):
    'expression :  PLUS '
    #p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression :  MINUS '
    #p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    #p[0] = p[1]


def p_term_times(p):
    'term :  TIMES '
    #p[0] = p[1] * p[3]


def p_term_div(p):
    'term :  DIVIDE '
    #p[0] = p[1] / p[3]

def p_valor(p):
    '''valor : INTV
            | ID'''


def p_term_factor(p):
    'term : factor'
    #p[0] = p[1]


def p_factor_num(p):
    'factor : INTV'
   # p[0] = p[1]


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    #p[0] = p[2]

    # Error rule for syntax errors


def p_error(p):
    print("Syntax error in input!")

    # Build the parser


parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)