
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND ASSIGN BOOLEAN BYTE CHAR COUNT DIVIDE DOUBLE ELSE EQUALS EQUALSM FALSE FIRST FLOAT FLOATV FOR FUNCTION GET GREATER GREATERE ID IF IN INT INTV LAST LCBRACKET LENGTH LIST LISTOF LONG LOWER LOWERE LPAREN LSBRACKET MINUS MODULE MUTABLELIST MUTABLELISTOF NOT NOTEQUALS NULL OR PLUS PRINTLN RCBRACKET RETURN RPAREN RSBRACKET SETOF SHORT STRING STRINGW TIMES TRUE VAL VAR WHILEcuerpo : sentencia  cuerpo : function  cuerpo : sentencia cuerpocuerpo : function cuerposentencia : asignacion \n                | estructuraControl\n                | bucles\n                | llamada\n                | declaracion instrucciones : LCBRACKET cuerpo RCBRACKET\n                | sentencia instruccionesF : LCBRACKET cuerpo retorno RCBRACKETinstruccionesF : LCBRACKET retorno RCBRACKETinstruccionesF : ':' dato LCBRACKET cuerpo retorno RCBRACKETinstruccionesF : ':' dato LCBRACKET retorno RCBRACKETretorno : RETURN expresion estructuraControl : IF LPAREN expresion RPAREN instrucciones estructuraControl : ELSE instrucciones bucles : while instrucciones\n                | for instrucciones while : WHILE LPAREN expresion RPAREN for : FOR LPAREN ID IN ID RPAREN function : FUNCTION ID LPAREN params RPAREN instruccionesFfunction : FUNCTION ID LPAREN RPAREN instruccionesFllamada : PRINTLN LPAREN expresion RPARENllamada : ID LPAREN args RPAREN llamada : ID LPAREN RPAREN llamada : ID '.' ID LPAREN args RPARENllamada : ID '.' ID LPAREN RPARENfunction : ID LSBRACKET expresion RSBRACKETdato : INT\n            | FLOAT\n            | BYTE\n            | SHORT\n            | DOUBLE\n            | ID\n            | LONG\n            | CHAR\n            | BOOLEAN\n            | LIST\n            | MUTABLELISTparams : ID ':' dato params : params ',' paramsargs : expresionargs : args ',' argsvalor : IDvalor : number\n            | STRINGvalor : TRUE\n            | FALSEvalor : NULLvalor : NOT valor declarador : VAR\n                | VALasignacion : ID ASSIGN expresion asignacion : declarador ID ASSIGN expresion declaracion : declarador ID llamada : LISTOF LPAREN params RPARENllamada : MUTABLELISTOF LPAREN params RPARENexpresion : llamadaexpresion : LPAREN expresion RPARENexpresion : valor expresion : expresion operadoresMat expresion expresion : expresion operadoresLog expresion operadoresLog :  OR\n                    | AND\n                    | EQUALS\n                    | NOTEQUALS\n                    | GREATER\n                    | LOWER\n                    | GREATERE\n                    | LOWEREoperadoresMat : MINUS\n                    | PLUS\n                    | TIMES\n                    | DIVIDE\n                    | MODULE number : INTV\n            | FLOATV llamada : ID '.' LENGTH LPAREN RPARENllamada : ID '.' EQUALSM LPAREN ID RPARENllamada : ID '.' EQUALSM LPAREN STRING RPARENllamada : ID '.' COUNT LPAREN RPARENllamada : ID '.' FIRST LPAREN RPARENllamada : ID '.' LAST LPAREN RPARENllamada : ID '.' GET LPAREN INTV RPARENllamada : ID '.' GET LPAREN ID RPAREN"
    
_lr_action_items = {'FUNCTION':([0,2,3,4,5,6,7,8,30,32,33,34,36,37,44,46,48,49,50,51,52,53,54,56,57,59,79,96,97,98,107,109,110,111,114,118,119,121,122,123,126,127,130,131,132,135,150,155,156,157,158,159,162,164,165,169,170,],[9,9,9,-5,-6,-7,-8,-9,-57,-18,9,-11,-19,-20,-46,-60,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,-30,-52,-46,-26,-56,-10,-25,-58,-59,-24,9,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,-28,-81,-82,-87,-86,-13,9,-12,-15,-14,]),'ID':([0,2,3,4,5,6,7,8,9,11,13,14,15,19,20,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,59,68,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,102,106,107,108,109,110,111,112,113,114,115,116,118,119,120,121,122,123,126,127,130,131,132,135,150,153,155,156,157,158,159,160,162,164,165,169,170,],[10,10,10,-5,-6,-7,-8,-9,25,30,35,35,35,-53,-54,44,44,44,61,-57,44,-18,10,-11,-19,-20,44,73,73,44,76,73,-46,-60,44,-62,-48,-78,-47,-49,-50,-51,97,-79,-55,-27,44,-30,44,44,-73,-74,-75,-76,-77,-65,-66,-67,-68,-69,-70,-71,-72,-52,-46,-26,44,44,128,133,-56,35,-10,-25,-58,73,137,-59,-21,149,-24,10,137,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,44,-28,-81,-82,-87,-86,-22,-13,10,-12,-15,-14,]),'IF':([0,2,3,4,5,6,7,8,13,14,15,30,32,33,34,36,37,44,46,48,49,50,51,52,53,54,56,57,59,79,96,97,98,107,108,109,110,111,114,115,118,119,121,122,123,126,127,130,131,132,135,150,155,156,157,158,159,160,162,164,165,169,170,],[12,12,12,-5,-6,-7,-8,-9,12,12,12,-57,-18,12,-11,-19,-20,-46,-60,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,-30,-52,-46,-26,-56,12,-10,-25,-58,-59,-21,-24,12,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,-28,-81,-82,-87,-86,-22,-13,12,-12,-15,-14,]),'ELSE':([0,2,3,4,5,6,7,8,13,14,15,30,32,33,34,36,37,44,46,48,49,50,51,52,53,54,56,57,59,79,96,97,98,107,108,109,110,111,114,115,118,119,121,122,123,126,127,130,131,132,135,150,155,156,157,158,159,160,162,164,165,169,170,],[13,13,13,-5,-6,-7,-8,-9,13,13,13,-57,-18,13,-11,-19,-20,-46,-60,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,-30,-52,-46,-26,-56,13,-10,-25,-58,-59,-21,-24,13,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,-28,-81,-82,-87,-86,-22,-13,13,-12,-15,-14,]),'PRINTLN':([0,2,3,4,5,6,7,8,13,14,15,26,27,28,30,31,32,33,34,36,37,38,41,44,46,47,48,49,50,51,52,53,54,56,57,59,68,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,107,108,109,110,111,114,115,118,119,121,122,123,126,127,130,131,132,135,150,153,155,156,157,158,159,160,162,164,165,169,170,],[16,16,16,-5,-6,-7,-8,-9,16,16,16,16,16,16,-57,16,-18,16,-11,-19,-20,16,16,-46,-60,16,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,16,-30,16,16,-73,-74,-75,-76,-77,-65,-66,-67,-68,-69,-70,-71,-72,-52,-46,-26,16,16,-56,16,-10,-25,-58,-59,-21,-24,16,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,16,-28,-81,-82,-87,-86,-22,-13,16,-12,-15,-14,]),'LISTOF':([0,2,3,4,5,6,7,8,13,14,15,26,27,28,30,31,32,33,34,36,37,38,41,44,46,47,48,49,50,51,52,53,54,56,57,59,68,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,107,108,109,110,111,114,115,118,119,121,122,123,126,127,130,131,132,135,150,153,155,156,157,158,159,160,162,164,165,169,170,],[17,17,17,-5,-6,-7,-8,-9,17,17,17,17,17,17,-57,17,-18,17,-11,-19,-20,17,17,-46,-60,17,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,17,-30,17,17,-73,-74,-75,-76,-77,-65,-66,-67,-68,-69,-70,-71,-72,-52,-46,-26,17,17,-56,17,-10,-25,-58,-59,-21,-24,17,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,17,-28,-81,-82,-87,-86,-22,-13,17,-12,-15,-14,]),'MUTABLELISTOF':([0,2,3,4,5,6,7,8,13,14,15,26,27,28,30,31,32,33,34,36,37,38,41,44,46,47,48,49,50,51,52,53,54,56,57,59,68,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,107,108,109,110,111,114,115,118,119,121,122,123,126,127,130,131,132,135,150,153,155,156,157,158,159,160,162,164,165,169,170,],[18,18,18,-5,-6,-7,-8,-9,18,18,18,18,18,18,-57,18,-18,18,-11,-19,-20,18,18,-46,-60,18,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,18,-30,18,18,-73,-74,-75,-76,-77,-65,-66,-67,-68,-69,-70,-71,-72,-52,-46,-26,18,18,-56,18,-10,-25,-58,-59,-21,-24,18,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,18,-28,-81,-82,-87,-86,-22,-13,18,-12,-15,-14,]),'VAR':([0,2,3,4,5,6,7,8,13,14,15,30,32,33,34,36,37,44,46,48,49,50,51,52,53,54,56,57,59,79,96,97,98,107,108,109,110,111,114,115,118,119,121,122,123,126,127,130,131,132,135,150,155,156,157,158,159,160,162,164,165,169,170,],[19,19,19,-5,-6,-7,-8,-9,19,19,19,-57,-18,19,-11,-19,-20,-46,-60,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,-30,-52,-46,-26,-56,19,-10,-25,-58,-59,-21,-24,19,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,-28,-81,-82,-87,-86,-22,-13,19,-12,-15,-14,]),'VAL':([0,2,3,4,5,6,7,8,13,14,15,30,32,33,34,36,37,44,46,48,49,50,51,52,53,54,56,57,59,79,96,97,98,107,108,109,110,111,114,115,118,119,121,122,123,126,127,130,131,132,135,150,155,156,157,158,159,160,162,164,165,169,170,],[20,20,20,-5,-6,-7,-8,-9,20,20,20,-57,-18,20,-11,-19,-20,-46,-60,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,-30,-52,-46,-26,-56,20,-10,-25,-58,-59,-21,-24,20,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,-28,-81,-82,-87,-86,-22,-13,20,-12,-15,-14,]),'WHILE':([0,2,3,4,5,6,7,8,13,14,15,30,32,33,34,36,37,44,46,48,49,50,51,52,53,54,56,57,59,79,96,97,98,107,108,109,110,111,114,115,118,119,121,122,123,126,127,130,131,132,135,150,155,156,157,158,159,160,162,164,165,169,170,],[21,21,21,-5,-6,-7,-8,-9,21,21,21,-57,-18,21,-11,-19,-20,-46,-60,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,-30,-52,-46,-26,-56,21,-10,-25,-58,-59,-21,-24,21,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,-28,-81,-82,-87,-86,-22,-13,21,-12,-15,-14,]),'FOR':([0,2,3,4,5,6,7,8,13,14,15,30,32,33,34,36,37,44,46,48,49,50,51,52,53,54,56,57,59,79,96,97,98,107,108,109,110,111,114,115,118,119,121,122,123,126,127,130,131,132,135,150,155,156,157,158,159,160,162,164,165,169,170,],[22,22,22,-5,-6,-7,-8,-9,22,22,22,-57,-18,22,-11,-19,-20,-46,-60,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,-30,-52,-46,-26,-56,22,-10,-25,-58,-59,-21,-24,22,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,-28,-81,-82,-87,-86,-22,-13,22,-12,-15,-14,]),'$end':([1,2,3,4,5,6,7,8,23,24,30,32,34,36,37,44,46,48,49,50,51,52,53,54,56,57,59,79,96,97,98,107,109,110,111,114,118,121,122,123,126,127,130,131,132,135,150,155,156,157,158,159,162,165,169,170,],[0,-1,-2,-5,-6,-7,-8,-9,-3,-4,-57,-18,-11,-19,-20,-46,-60,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,-30,-52,-46,-26,-56,-10,-25,-58,-59,-24,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,-28,-81,-82,-87,-86,-13,-12,-15,-14,]),'RCBRACKET':([2,3,4,5,6,7,8,23,24,30,32,34,36,37,44,46,48,49,50,51,52,53,54,56,57,59,70,79,96,97,98,107,109,110,111,114,118,121,122,123,126,127,130,131,132,135,150,152,155,156,157,158,159,161,162,163,165,167,168,169,170,],[-1,-2,-5,-6,-7,-8,-9,-3,-4,-57,-18,-11,-19,-20,-46,-60,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,109,-30,-52,-46,-26,-56,-10,-25,-58,-59,-24,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,162,-28,-81,-82,-87,-86,165,-13,-16,-12,169,170,-15,-14,]),'RETURN':([2,3,4,5,6,7,8,23,24,30,32,34,36,37,44,46,48,49,50,51,52,53,54,56,57,59,79,96,97,98,107,109,110,111,114,118,119,121,122,123,126,127,130,131,132,135,150,151,155,156,157,158,159,162,164,165,166,169,170,],[-1,-2,-5,-6,-7,-8,-9,-3,-4,-57,-18,-11,-19,-20,-46,-60,-62,-48,-78,-47,-49,-50,-51,-79,-55,-27,-30,-52,-46,-26,-56,-10,-25,-58,-59,-24,153,-63,-64,-61,-29,-80,-83,-84,-85,-17,-23,153,-28,-81,-82,-87,-86,-13,153,-12,153,-15,-14,]),'LSBRACKET':([10,],[26,]),'ASSIGN':([10,30,35,],[27,68,27,]),'LPAREN':([10,12,16,17,18,21,22,25,26,27,28,31,35,38,41,44,47,61,62,63,64,65,66,67,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,153,],[28,31,38,39,40,41,42,43,47,47,47,47,28,47,47,28,47,100,101,102,103,104,105,106,47,47,47,-73,-74,-75,-76,-77,-65,-66,-67,-68,-69,-70,-71,-72,47,47,47,]),'.':([10,35,44,],[29,29,29,]),'LCBRACKET':([13,14,15,78,108,115,117,137,139,140,141,142,143,144,145,146,147,148,154,160,],[33,33,33,119,33,-21,119,-36,-31,-32,-33,-34,-35,-37,-38,-39,-40,-41,164,-22,]),'STRING':([26,27,28,31,38,41,47,55,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,102,153,],[49,49,49,49,49,49,49,49,49,49,49,-73,-74,-75,-76,-77,-65,-66,-67,-68,-69,-70,-71,-72,49,49,129,49,]),'TRUE':([26,27,28,31,38,41,47,55,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,153,],[52,52,52,52,52,52,52,52,52,52,52,-73,-74,-75,-76,-77,-65,-66,-67,-68,-69,-70,-71,-72,52,52,52,]),'FALSE':([26,27,28,31,38,41,47,55,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,153,],[53,53,53,53,53,53,53,53,53,53,53,-73,-74,-75,-76,-77,-65,-66,-67,-68,-69,-70,-71,-72,53,53,53,]),'NULL':([26,27,28,31,38,41,47,55,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,153,],[54,54,54,54,54,54,54,54,54,54,54,-73,-74,-75,-76,-77,-65,-66,-67,-68,-69,-70,-71,-72,54,54,54,]),'NOT':([26,27,28,31,38,41,47,55,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,153,],[55,55,55,55,55,55,55,55,55,55,55,-73,-74,-75,-76,-77,-65,-66,-67,-68,-69,-70,-71,-72,55,55,55,]),'INTV':([26,27,28,31,38,41,47,55,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,106,153,],[50,50,50,50,50,50,50,50,50,50,50,-73,-74,-75,-76,-77,-65,-66,-67,-68,-69,-70,-71,-72,50,50,134,50,]),'FLOATV':([26,27,28,31,38,41,47,55,68,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,153,],[56,56,56,56,56,56,56,56,56,56,56,-73,-74,-75,-76,-77,-65,-66,-67,-68,-69,-70,-71,-72,56,56,56,]),'RPAREN':([28,43,44,46,48,49,50,51,52,53,54,56,58,59,60,69,71,72,74,75,77,95,96,97,98,100,101,103,104,105,110,111,114,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,138,139,140,141,142,143,144,145,146,147,148,149,155,156,157,158,159,],[59,78,-46,-60,-62,-48,-78,-47,-49,-50,-51,-79,98,-27,-44,108,110,111,114,115,117,123,-52,-46,-26,126,127,130,131,132,-25,-58,-59,-63,-64,-61,-45,155,-29,-80,156,157,-83,-84,-85,158,159,-43,-36,-42,-31,-32,-33,-34,-35,-37,-38,-39,-40,-41,160,-28,-81,-82,-87,-86,]),'LENGTH':([29,],[62,]),'EQUALSM':([29,],[63,]),'COUNT':([29,],[64,]),'FIRST':([29,],[65,]),'LAST':([29,],[66,]),'GET':([29,],[67,]),'RSBRACKET':([44,45,46,48,49,50,51,52,53,54,56,59,96,97,98,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,],[-46,79,-60,-62,-48,-78,-47,-49,-50,-51,-79,-27,-52,-46,-26,-25,-58,-59,-63,-64,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,]),'MINUS':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,82,-60,-62,-48,-78,-47,-49,-50,-51,-79,82,-27,82,82,82,82,82,-52,-46,-26,82,-25,-58,-59,82,82,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,82,]),'PLUS':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,83,-60,-62,-48,-78,-47,-49,-50,-51,-79,83,-27,83,83,83,83,83,-52,-46,-26,83,-25,-58,-59,83,83,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,83,]),'TIMES':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,84,-60,-62,-48,-78,-47,-49,-50,-51,-79,84,-27,84,84,84,84,84,-52,-46,-26,84,-25,-58,-59,84,84,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,84,]),'DIVIDE':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,85,-60,-62,-48,-78,-47,-49,-50,-51,-79,85,-27,85,85,85,85,85,-52,-46,-26,85,-25,-58,-59,85,85,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,85,]),'MODULE':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,86,-60,-62,-48,-78,-47,-49,-50,-51,-79,86,-27,86,86,86,86,86,-52,-46,-26,86,-25,-58,-59,86,86,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,86,]),'OR':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,87,-60,-62,-48,-78,-47,-49,-50,-51,-79,87,-27,87,87,87,87,87,-52,-46,-26,87,-25,-58,-59,87,87,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,87,]),'AND':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,88,-60,-62,-48,-78,-47,-49,-50,-51,-79,88,-27,88,88,88,88,88,-52,-46,-26,88,-25,-58,-59,88,88,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,88,]),'EQUALS':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,89,-60,-62,-48,-78,-47,-49,-50,-51,-79,89,-27,89,89,89,89,89,-52,-46,-26,89,-25,-58,-59,89,89,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,89,]),'NOTEQUALS':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,90,-60,-62,-48,-78,-47,-49,-50,-51,-79,90,-27,90,90,90,90,90,-52,-46,-26,90,-25,-58,-59,90,90,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,90,]),'GREATER':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,91,-60,-62,-48,-78,-47,-49,-50,-51,-79,91,-27,91,91,91,91,91,-52,-46,-26,91,-25,-58,-59,91,91,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,91,]),'LOWER':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,92,-60,-62,-48,-78,-47,-49,-50,-51,-79,92,-27,92,92,92,92,92,-52,-46,-26,92,-25,-58,-59,92,92,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,92,]),'GREATERE':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,93,-60,-62,-48,-78,-47,-49,-50,-51,-79,93,-27,93,93,93,93,93,-52,-46,-26,93,-25,-58,-59,93,93,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,93,]),'LOWERE':([44,45,46,48,49,50,51,52,53,54,56,57,59,60,69,71,75,95,96,97,98,107,110,111,114,121,122,123,126,127,130,131,132,155,156,157,158,159,163,],[-46,94,-60,-62,-48,-78,-47,-49,-50,-51,-79,94,-27,94,94,94,94,94,-52,-46,-26,94,-25,-58,-59,94,94,-61,-29,-80,-83,-84,-85,-28,-81,-82,-87,-86,94,]),',':([44,46,48,49,50,51,52,53,54,56,58,59,60,72,74,77,96,97,98,110,111,114,121,122,123,124,125,126,127,130,131,132,136,137,138,139,140,141,142,143,144,145,146,147,148,155,156,157,158,159,],[-46,-60,-62,-48,-78,-47,-49,-50,-51,-79,99,-27,-44,112,112,112,-52,-46,-26,-25,-58,-59,-63,-64,-61,99,99,-29,-80,-83,-84,-85,112,-36,-42,-31,-32,-33,-34,-35,-37,-38,-39,-40,-41,-28,-81,-82,-87,-86,]),':':([73,78,117,],[113,120,120,]),'IN':([76,],[116,]),'INT':([113,120,],[139,139,]),'FLOAT':([113,120,],[140,140,]),'BYTE':([113,120,],[141,141,]),'SHORT':([113,120,],[142,142,]),'DOUBLE':([113,120,],[143,143,]),'LONG':([113,120,],[144,144,]),'CHAR':([113,120,],[145,145,]),'BOOLEAN':([113,120,],[146,146,]),'LIST':([113,120,],[147,147,]),'MUTABLELIST':([113,120,],[148,148,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,2,3,33,119,164,],[1,23,24,70,151,166,]),'sentencia':([0,2,3,13,14,15,33,108,119,164,],[2,2,2,34,34,34,2,34,2,2,]),'function':([0,2,3,33,119,164,],[3,3,3,3,3,3,]),'asignacion':([0,2,3,13,14,15,33,108,119,164,],[4,4,4,4,4,4,4,4,4,4,]),'estructuraControl':([0,2,3,13,14,15,33,108,119,164,],[5,5,5,5,5,5,5,5,5,5,]),'bucles':([0,2,3,13,14,15,33,108,119,164,],[6,6,6,6,6,6,6,6,6,6,]),'llamada':([0,2,3,13,14,15,26,27,28,31,33,38,41,47,68,80,81,99,100,108,119,153,164,],[7,7,7,7,7,7,46,46,46,46,7,46,46,46,46,46,46,46,46,7,7,46,7,]),'declaracion':([0,2,3,13,14,15,33,108,119,164,],[8,8,8,8,8,8,8,8,8,8,]),'declarador':([0,2,3,13,14,15,33,108,119,164,],[11,11,11,11,11,11,11,11,11,11,]),'while':([0,2,3,13,14,15,33,108,119,164,],[14,14,14,14,14,14,14,14,14,14,]),'for':([0,2,3,13,14,15,33,108,119,164,],[15,15,15,15,15,15,15,15,15,15,]),'instrucciones':([13,14,15,108,],[32,36,37,135,]),'expresion':([26,27,28,31,38,41,47,68,80,81,99,100,153,],[45,57,60,69,71,75,95,107,121,122,60,60,163,]),'valor':([26,27,28,31,38,41,47,55,68,80,81,99,100,153,],[48,48,48,48,48,48,48,96,48,48,48,48,48,48,]),'number':([26,27,28,31,38,41,47,55,68,80,81,99,100,153,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'args':([28,99,100,],[58,124,125,]),'params':([39,40,43,112,],[72,74,77,136,]),'operadoresMat':([45,57,60,69,71,75,95,107,121,122,163,],[80,80,80,80,80,80,80,80,80,80,80,]),'operadoresLog':([45,57,60,69,71,75,95,107,121,122,163,],[81,81,81,81,81,81,81,81,81,81,81,]),'instruccionesF':([78,117,],[118,150,]),'dato':([113,120,],[138,154,]),'retorno':([119,151,164,166,],[152,161,167,168,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> sentencia','cuerpo',1,'p_cuerpo','sintactico.py',8),
  ('cuerpo -> function','cuerpo',1,'p_cuerpo_funcion_sola','sintactico.py',12),
  ('cuerpo -> sentencia cuerpo','cuerpo',2,'p_cuerpoR','sintactico.py',16),
  ('cuerpo -> function cuerpo','cuerpo',2,'p_cuerpo_funcion','sintactico.py',20),
  ('sentencia -> asignacion','sentencia',1,'p_sentencia','sintactico.py',25),
  ('sentencia -> estructuraControl','sentencia',1,'p_sentencia','sintactico.py',26),
  ('sentencia -> bucles','sentencia',1,'p_sentencia','sintactico.py',27),
  ('sentencia -> llamada','sentencia',1,'p_sentencia','sintactico.py',28),
  ('sentencia -> declaracion','sentencia',1,'p_sentencia','sintactico.py',29),
  ('instrucciones -> LCBRACKET cuerpo RCBRACKET','instrucciones',3,'p_instrucciones','sintactico.py',33),
  ('instrucciones -> sentencia','instrucciones',1,'p_instrucciones','sintactico.py',34),
  ('instruccionesF -> LCBRACKET cuerpo retorno RCBRACKET','instruccionesF',4,'p_instrucciones_funcion','sintactico.py',37),
  ('instruccionesF -> LCBRACKET retorno RCBRACKET','instruccionesF',3,'p_instrucciones_funcion_retorno','sintactico.py',40),
  ('instruccionesF -> : dato LCBRACKET cuerpo retorno RCBRACKET','instruccionesF',6,'p_instrucciones_funcion_dato','sintactico.py',44),
  ('instruccionesF -> : dato LCBRACKET retorno RCBRACKET','instruccionesF',5,'p_instrucciones_funcion_retorno_dato','sintactico.py',48),
  ('retorno -> RETURN expresion','retorno',2,'p_retorno','sintactico.py',51),
  ('estructuraControl -> IF LPAREN expresion RPAREN instrucciones','estructuraControl',5,'p_estructuraControlIf','sintactico.py',56),
  ('estructuraControl -> ELSE instrucciones','estructuraControl',2,'p_estructuraControlElse','sintactico.py',59),
  ('bucles -> while instrucciones','bucles',2,'p_bucles','sintactico.py',62),
  ('bucles -> for instrucciones','bucles',2,'p_bucles','sintactico.py',63),
  ('while -> WHILE LPAREN expresion RPAREN','while',4,'p_while','sintactico.py',68),
  ('for -> FOR LPAREN ID IN ID RPAREN','for',6,'p_for','sintactico.py',72),
  ('function -> FUNCTION ID LPAREN params RPAREN instruccionesF','function',6,'p_function','sintactico.py',77),
  ('function -> FUNCTION ID LPAREN RPAREN instruccionesF','function',5,'p_function_sin_params','sintactico.py',80),
  ('llamada -> PRINTLN LPAREN expresion RPAREN','llamada',4,'p_print','sintactico.py',83),
  ('llamada -> ID LPAREN args RPAREN','llamada',4,'p_llamada_funcion','sintactico.py',88),
  ('llamada -> ID LPAREN RPAREN','llamada',3,'p_llamada_funcion_sin_params','sintactico.py',92),
  ('llamada -> ID . ID LPAREN args RPAREN','llamada',6,'p_llamada_objeto','sintactico.py',96),
  ('llamada -> ID . ID LPAREN RPAREN','llamada',5,'p_llamada_objeto_sin_params','sintactico.py',99),
  ('function -> ID LSBRACKET expresion RSBRACKET','function',4,'p_index','sintactico.py',103),
  ('dato -> INT','dato',1,'p_dato','sintactico.py',108),
  ('dato -> FLOAT','dato',1,'p_dato','sintactico.py',109),
  ('dato -> BYTE','dato',1,'p_dato','sintactico.py',110),
  ('dato -> SHORT','dato',1,'p_dato','sintactico.py',111),
  ('dato -> DOUBLE','dato',1,'p_dato','sintactico.py',112),
  ('dato -> ID','dato',1,'p_dato','sintactico.py',113),
  ('dato -> LONG','dato',1,'p_dato','sintactico.py',114),
  ('dato -> CHAR','dato',1,'p_dato','sintactico.py',115),
  ('dato -> BOOLEAN','dato',1,'p_dato','sintactico.py',116),
  ('dato -> LIST','dato',1,'p_dato','sintactico.py',117),
  ('dato -> MUTABLELIST','dato',1,'p_dato','sintactico.py',118),
  ('params -> ID : dato','params',3,'p_params','sintactico.py',122),
  ('params -> params , params','params',3,'p_params2','sintactico.py',126),
  ('args -> expresion','args',1,'p_args','sintactico.py',130),
  ('args -> args , args','args',3,'p_args2','sintactico.py',134),
  ('valor -> ID','valor',1,'p_valor_id','sintactico.py',139),
  ('valor -> number','valor',1,'p_valor','sintactico.py',143),
  ('valor -> STRING','valor',1,'p_valor','sintactico.py',144),
  ('valor -> TRUE','valor',1,'p_valor_bool','sintactico.py',148),
  ('valor -> FALSE','valor',1,'p_valor_bool','sintactico.py',149),
  ('valor -> NULL','valor',1,'p_valor_null','sintactico.py',157),
  ('valor -> NOT valor','valor',2,'p_valor_negado','sintactico.py',162),
  ('declarador -> VAR','declarador',1,'p_declarador','sintactico.py',167),
  ('declarador -> VAL','declarador',1,'p_declarador','sintactico.py',168),
  ('asignacion -> ID ASSIGN expresion','asignacion',3,'p_asignacion','sintactico.py',172),
  ('asignacion -> declarador ID ASSIGN expresion','asignacion',4,'p_asignacion_declarando','sintactico.py',183),
  ('declaracion -> declarador ID','declaracion',2,'p_declaracion','sintactico.py',190),
  ('llamada -> LISTOF LPAREN params RPAREN','llamada',4,'p_creacion_lista','sintactico.py',195),
  ('llamada -> MUTABLELISTOF LPAREN params RPAREN','llamada',4,'p_creacion_lista_mutable','sintactico.py',199),
  ('expresion -> llamada','expresion',1,'p_expresion_llamada','sintactico.py',203),
  ('expresion -> LPAREN expresion RPAREN','expresion',3,'p_exresion','sintactico.py',208),
  ('expresion -> valor','expresion',1,'p_expesion','sintactico.py',212),
  ('expresion -> expresion operadoresMat expresion','expresion',3,'p_expresion_matematica','sintactico.py',217),
  ('expresion -> expresion operadoresLog expresion','expresion',3,'p_expresion_logica','sintactico.py',234),
  ('operadoresLog -> OR','operadoresLog',1,'p_operadores_log','sintactico.py',253),
  ('operadoresLog -> AND','operadoresLog',1,'p_operadores_log','sintactico.py',254),
  ('operadoresLog -> EQUALS','operadoresLog',1,'p_operadores_log','sintactico.py',255),
  ('operadoresLog -> NOTEQUALS','operadoresLog',1,'p_operadores_log','sintactico.py',256),
  ('operadoresLog -> GREATER','operadoresLog',1,'p_operadores_log','sintactico.py',257),
  ('operadoresLog -> LOWER','operadoresLog',1,'p_operadores_log','sintactico.py',258),
  ('operadoresLog -> GREATERE','operadoresLog',1,'p_operadores_log','sintactico.py',259),
  ('operadoresLog -> LOWERE','operadoresLog',1,'p_operadores_log','sintactico.py',260),
  ('operadoresMat -> MINUS','operadoresMat',1,'p_operadores_mat','sintactico.py',265),
  ('operadoresMat -> PLUS','operadoresMat',1,'p_operadores_mat','sintactico.py',266),
  ('operadoresMat -> TIMES','operadoresMat',1,'p_operadores_mat','sintactico.py',267),
  ('operadoresMat -> DIVIDE','operadoresMat',1,'p_operadores_mat','sintactico.py',268),
  ('operadoresMat -> MODULE','operadoresMat',1,'p_operadores_mat','sintactico.py',269),
  ('number -> INTV','number',1,'p_number','sintactico.py',277),
  ('number -> FLOATV','number',1,'p_number','sintactico.py',278),
  ('llamada -> ID . LENGTH LPAREN RPAREN','llamada',5,'p_string_length','sintactico.py',282),
  ('llamada -> ID . EQUALSM LPAREN ID RPAREN','llamada',6,'p_string_equals','sintactico.py',291),
  ('llamada -> ID . EQUALSM LPAREN STRING RPAREN','llamada',6,'p_string_equals2','sintactico.py',301),
  ('llamada -> ID . COUNT LPAREN RPAREN','llamada',5,'p_list_count','sintactico.py',309),
  ('llamada -> ID . FIRST LPAREN RPAREN','llamada',5,'p_list_first','sintactico.py',317),
  ('llamada -> ID . LAST LPAREN RPAREN','llamada',5,'p_list_last','sintactico.py',325),
  ('llamada -> ID . GET LPAREN INTV RPAREN','llamada',6,'p_list_get','sintactico.py',334),
  ('llamada -> ID . GET LPAREN ID RPAREN','llamada',6,'p_list_get2','sintactico.py',342),
]
