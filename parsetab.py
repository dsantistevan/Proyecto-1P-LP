
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND ASSIGN BOOLEAN BYTE CHAR DIVIDE DOUBLE ELSE EQUALS FALSE FLOAT FLOATV FOR FUNCTION GREATER ID IF IN INT INTV LCBRACKET LONG LOWER LPAREN LSBRACKET MINUS MODULE NOT NOTEQUALS NULL OR PLUS PRINTLN RCBRACKET RETURN RPAREN RSBRACKET SHORT STRING TIMES TRUE VAL VAR WHILEcuerpo : sentencia  cuerpo : function  cuerpo : sentencia cuerpocuerpo : function cuerposentencia : asignacion \n                | estructuraControl\n                | bucles\n                | llamada\n                | declaracion instrucciones : LCBRACKET cuerpo RCBRACKET\n                | sentencia instruccionesF : LCBRACKET cuerpo retorno RCBRACKETinstruccionesF : LCBRACKET retorno RCBRACKETretorno : RETURN expresion estructuraControl : IF LPAREN expresion RPAREN instrucciones estructuraControl : ELSE instrucciones bucles : while instrucciones\n                | for instrucciones while : WHILE LPAREN expresion RPAREN for : FOR LPAREN ID IN ID RPAREN function : FUNCTION ID LPAREN params RPAREN instruccionesFfunction : FUNCTION ID LPAREN RPAREN instruccionesFllamada : PRINTLN LPAREN expresion RPARENllamada : ID LPAREN args RPAREN llamada : ID LPAREN RPAREN function : ID LSBRACKET valor RSBRACKETdato : INT\n            | FLOAT\n            | BYTE\n            | SHORT\n            | DOUBLE\n            | ID\n            | LONG\n            | CHAR\n            | BOOLEANparams : ID ':' dato params : params ',' paramsargs : valorargs : args ',' argsvalor : IDvalor : number\n            | STRINGvalor : TRUE\n            | FALSEvalor : NULLvalor : NOT valor declarador : VAR\n                | VALasignacion : ID ASSIGN expresion asignacion : declarador ID ASSIGN expresion declaracion : declarador ID expresion : LPAREN expresion RPARENexpresion : valor expresion : expresion operadoresMat expresion expresion : expresion operadoresLog expresion operadoresLog :  OR\n                    | AND\n                    | EQUALS\n                    | NOTEQUALS\n                    | GREATER\n                    | LOWER\n                    | GREATER ASSIGN\n                    | LOWER ASSIGNoperadoresMat : MINUS\n                    | PLUS\n                    | TIMES\n                    | DIVIDE\n                    | MODULE number : INTV\n            | FLOATV "
    
_lr_action_items = {'FUNCTION':([0,2,3,4,5,6,7,8,27,29,30,31,33,34,39,41,42,43,44,45,47,48,49,51,53,64,65,80,82,84,85,91,92,93,94,97,99,111,118,120,],[9,9,9,-5,-6,-7,-8,-9,-51,-16,9,-11,-17,-18,-40,-41,-42,-43,-44,-45,-69,-70,-49,-53,-25,-26,-46,-24,-50,-10,-23,-22,9,-54,-55,-52,-15,-21,-13,-12,]),'ID':([0,2,3,4,5,6,7,8,9,11,13,14,15,17,18,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,53,55,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,88,90,91,92,93,94,95,96,97,99,111,115,116,118,120,],[10,10,10,-5,-6,-7,-8,-9,23,27,32,32,32,-47,-48,39,39,39,-51,39,-16,10,-11,-17,-18,39,39,60,61,-40,-41,-42,-43,-44,-45,39,-69,-70,-49,39,-53,-25,39,-26,-46,39,39,-64,-65,-66,-67,-68,-56,-57,-58,-59,-60,-61,-24,39,-50,32,-10,-23,-19,100,101,61,-22,10,-54,-55,-62,-63,-52,-15,-21,39,-20,-13,-12,]),'IF':([0,2,3,4,5,6,7,8,13,14,15,27,29,30,31,33,34,39,41,42,43,44,45,47,48,49,51,53,64,65,80,82,83,84,85,86,91,92,93,94,97,99,111,116,118,120,],[12,12,12,-5,-6,-7,-8,-9,12,12,12,-51,-16,12,-11,-17,-18,-40,-41,-42,-43,-44,-45,-69,-70,-49,-53,-25,-26,-46,-24,-50,12,-10,-23,-19,-22,12,-54,-55,-52,-15,-21,-20,-13,-12,]),'ELSE':([0,2,3,4,5,6,7,8,13,14,15,27,29,30,31,33,34,39,41,42,43,44,45,47,48,49,51,53,64,65,80,82,83,84,85,86,91,92,93,94,97,99,111,116,118,120,],[13,13,13,-5,-6,-7,-8,-9,13,13,13,-51,-16,13,-11,-17,-18,-40,-41,-42,-43,-44,-45,-69,-70,-49,-53,-25,-26,-46,-24,-50,13,-10,-23,-19,-22,13,-54,-55,-52,-15,-21,-20,-13,-12,]),'PRINTLN':([0,2,3,4,5,6,7,8,13,14,15,27,29,30,31,33,34,39,41,42,43,44,45,47,48,49,51,53,64,65,80,82,83,84,85,86,91,92,93,94,97,99,111,116,118,120,],[16,16,16,-5,-6,-7,-8,-9,16,16,16,-51,-16,16,-11,-17,-18,-40,-41,-42,-43,-44,-45,-69,-70,-49,-53,-25,-26,-46,-24,-50,16,-10,-23,-19,-22,16,-54,-55,-52,-15,-21,-20,-13,-12,]),'VAR':([0,2,3,4,5,6,7,8,13,14,15,27,29,30,31,33,34,39,41,42,43,44,45,47,48,49,51,53,64,65,80,82,83,84,85,86,91,92,93,94,97,99,111,116,118,120,],[17,17,17,-5,-6,-7,-8,-9,17,17,17,-51,-16,17,-11,-17,-18,-40,-41,-42,-43,-44,-45,-69,-70,-49,-53,-25,-26,-46,-24,-50,17,-10,-23,-19,-22,17,-54,-55,-52,-15,-21,-20,-13,-12,]),'VAL':([0,2,3,4,5,6,7,8,13,14,15,27,29,30,31,33,34,39,41,42,43,44,45,47,48,49,51,53,64,65,80,82,83,84,85,86,91,92,93,94,97,99,111,116,118,120,],[18,18,18,-5,-6,-7,-8,-9,18,18,18,-51,-16,18,-11,-17,-18,-40,-41,-42,-43,-44,-45,-69,-70,-49,-53,-25,-26,-46,-24,-50,18,-10,-23,-19,-22,18,-54,-55,-52,-15,-21,-20,-13,-12,]),'WHILE':([0,2,3,4,5,6,7,8,13,14,15,27,29,30,31,33,34,39,41,42,43,44,45,47,48,49,51,53,64,65,80,82,83,84,85,86,91,92,93,94,97,99,111,116,118,120,],[19,19,19,-5,-6,-7,-8,-9,19,19,19,-51,-16,19,-11,-17,-18,-40,-41,-42,-43,-44,-45,-69,-70,-49,-53,-25,-26,-46,-24,-50,19,-10,-23,-19,-22,19,-54,-55,-52,-15,-21,-20,-13,-12,]),'FOR':([0,2,3,4,5,6,7,8,13,14,15,27,29,30,31,33,34,39,41,42,43,44,45,47,48,49,51,53,64,65,80,82,83,84,85,86,91,92,93,94,97,99,111,116,118,120,],[20,20,20,-5,-6,-7,-8,-9,20,20,20,-51,-16,20,-11,-17,-18,-40,-41,-42,-43,-44,-45,-69,-70,-49,-53,-25,-26,-46,-24,-50,20,-10,-23,-19,-22,20,-54,-55,-52,-15,-21,-20,-13,-12,]),'$end':([1,2,3,4,5,6,7,8,21,22,27,29,31,33,34,39,41,42,43,44,45,47,48,49,51,53,64,65,80,82,84,85,91,93,94,97,99,111,118,120,],[0,-1,-2,-5,-6,-7,-8,-9,-3,-4,-51,-16,-11,-17,-18,-40,-41,-42,-43,-44,-45,-69,-70,-49,-53,-25,-26,-46,-24,-50,-10,-23,-22,-54,-55,-52,-15,-21,-13,-12,]),'RCBRACKET':([2,3,4,5,6,7,8,21,22,27,29,31,33,34,39,41,42,43,44,45,47,48,49,51,53,57,64,65,80,82,84,85,91,93,94,97,99,111,114,117,118,119,120,],[-1,-2,-5,-6,-7,-8,-9,-3,-4,-51,-16,-11,-17,-18,-40,-41,-42,-43,-44,-45,-69,-70,-49,-53,-25,84,-26,-46,-24,-50,-10,-23,-22,-54,-55,-52,-15,-21,118,120,-13,-14,-12,]),'RETURN':([2,3,4,5,6,7,8,21,22,27,29,31,33,34,39,41,42,43,44,45,47,48,49,51,53,64,65,80,82,84,85,91,92,93,94,97,99,111,113,118,120,],[-1,-2,-5,-6,-7,-8,-9,-3,-4,-51,-16,-11,-17,-18,-40,-41,-42,-43,-44,-45,-69,-70,-49,-53,-25,-26,-46,-24,-50,-10,-23,-22,115,-54,-55,-52,-15,-21,115,-13,-12,]),'LSBRACKET':([10,],[24,]),'ASSIGN':([10,27,32,77,78,],[25,55,25,95,96,]),'LPAREN':([10,12,16,19,20,23,25,28,32,35,36,50,55,66,67,68,69,70,71,72,73,74,75,76,77,78,95,96,115,],[26,28,35,36,37,38,50,50,26,50,50,50,50,50,50,-64,-65,-66,-67,-68,-56,-57,-58,-59,-60,-61,-62,-63,50,]),'LCBRACKET':([13,14,15,63,83,86,89,116,],[30,30,30,92,30,-19,92,-20,]),'STRING':([24,25,26,28,35,36,46,50,55,66,67,68,69,70,71,72,73,74,75,76,77,78,81,95,96,115,],[42,42,42,42,42,42,42,42,42,42,42,-64,-65,-66,-67,-68,-56,-57,-58,-59,-60,-61,42,-62,-63,42,]),'TRUE':([24,25,26,28,35,36,46,50,55,66,67,68,69,70,71,72,73,74,75,76,77,78,81,95,96,115,],[43,43,43,43,43,43,43,43,43,43,43,-64,-65,-66,-67,-68,-56,-57,-58,-59,-60,-61,43,-62,-63,43,]),'FALSE':([24,25,26,28,35,36,46,50,55,66,67,68,69,70,71,72,73,74,75,76,77,78,81,95,96,115,],[44,44,44,44,44,44,44,44,44,44,44,-64,-65,-66,-67,-68,-56,-57,-58,-59,-60,-61,44,-62,-63,44,]),'NULL':([24,25,26,28,35,36,46,50,55,66,67,68,69,70,71,72,73,74,75,76,77,78,81,95,96,115,],[45,45,45,45,45,45,45,45,45,45,45,-64,-65,-66,-67,-68,-56,-57,-58,-59,-60,-61,45,-62,-63,45,]),'NOT':([24,25,26,28,35,36,46,50,55,66,67,68,69,70,71,72,73,74,75,76,77,78,81,95,96,115,],[46,46,46,46,46,46,46,46,46,46,46,-64,-65,-66,-67,-68,-56,-57,-58,-59,-60,-61,46,-62,-63,46,]),'INTV':([24,25,26,28,35,36,46,50,55,66,67,68,69,70,71,72,73,74,75,76,77,78,81,95,96,115,],[47,47,47,47,47,47,47,47,47,47,47,-64,-65,-66,-67,-68,-56,-57,-58,-59,-60,-61,47,-62,-63,47,]),'FLOATV':([24,25,26,28,35,36,46,50,55,66,67,68,69,70,71,72,73,74,75,76,77,78,81,95,96,115,],[48,48,48,48,48,48,48,48,48,48,48,-64,-65,-66,-67,-68,-56,-57,-58,-59,-60,-61,48,-62,-63,48,]),'RPAREN':([26,38,39,41,42,43,44,45,47,48,51,52,54,56,58,59,62,65,79,93,94,97,98,100,101,102,103,104,105,106,107,108,109,110,112,],[53,63,-40,-41,-42,-43,-44,-45,-69,-70,-53,80,-38,83,85,86,89,-46,97,-54,-55,-52,-39,116,-32,-36,-27,-28,-29,-30,-31,-33,-34,-35,-37,]),'RSBRACKET':([39,40,41,42,43,44,45,47,48,65,],[-40,64,-41,-42,-43,-44,-45,-69,-70,-46,]),'MINUS':([39,41,42,43,44,45,47,48,49,51,56,58,59,65,79,82,93,94,97,119,],[-40,-41,-42,-43,-44,-45,-69,-70,68,-53,68,68,68,-46,68,68,68,68,-52,68,]),'PLUS':([39,41,42,43,44,45,47,48,49,51,56,58,59,65,79,82,93,94,97,119,],[-40,-41,-42,-43,-44,-45,-69,-70,69,-53,69,69,69,-46,69,69,69,69,-52,69,]),'TIMES':([39,41,42,43,44,45,47,48,49,51,56,58,59,65,79,82,93,94,97,119,],[-40,-41,-42,-43,-44,-45,-69,-70,70,-53,70,70,70,-46,70,70,70,70,-52,70,]),'DIVIDE':([39,41,42,43,44,45,47,48,49,51,56,58,59,65,79,82,93,94,97,119,],[-40,-41,-42,-43,-44,-45,-69,-70,71,-53,71,71,71,-46,71,71,71,71,-52,71,]),'MODULE':([39,41,42,43,44,45,47,48,49,51,56,58,59,65,79,82,93,94,97,119,],[-40,-41,-42,-43,-44,-45,-69,-70,72,-53,72,72,72,-46,72,72,72,72,-52,72,]),'OR':([39,41,42,43,44,45,47,48,49,51,56,58,59,65,79,82,93,94,97,119,],[-40,-41,-42,-43,-44,-45,-69,-70,73,-53,73,73,73,-46,73,73,73,73,-52,73,]),'AND':([39,41,42,43,44,45,47,48,49,51,56,58,59,65,79,82,93,94,97,119,],[-40,-41,-42,-43,-44,-45,-69,-70,74,-53,74,74,74,-46,74,74,74,74,-52,74,]),'EQUALS':([39,41,42,43,44,45,47,48,49,51,56,58,59,65,79,82,93,94,97,119,],[-40,-41,-42,-43,-44,-45,-69,-70,75,-53,75,75,75,-46,75,75,75,75,-52,75,]),'NOTEQUALS':([39,41,42,43,44,45,47,48,49,51,56,58,59,65,79,82,93,94,97,119,],[-40,-41,-42,-43,-44,-45,-69,-70,76,-53,76,76,76,-46,76,76,76,76,-52,76,]),'GREATER':([39,41,42,43,44,45,47,48,49,51,56,58,59,65,79,82,93,94,97,119,],[-40,-41,-42,-43,-44,-45,-69,-70,77,-53,77,77,77,-46,77,77,77,77,-52,77,]),'LOWER':([39,41,42,43,44,45,47,48,49,51,56,58,59,65,79,82,93,94,97,119,],[-40,-41,-42,-43,-44,-45,-69,-70,78,-53,78,78,78,-46,78,78,78,78,-52,78,]),',':([39,41,42,43,44,45,47,48,52,54,62,65,98,101,102,103,104,105,106,107,108,109,110,112,],[-40,-41,-42,-43,-44,-45,-69,-70,81,-38,90,-46,81,-32,-36,-27,-28,-29,-30,-31,-33,-34,-35,90,]),'IN':([60,],[87,]),':':([61,],[88,]),'INT':([88,],[103,]),'FLOAT':([88,],[104,]),'BYTE':([88,],[105,]),'SHORT':([88,],[106,]),'DOUBLE':([88,],[107,]),'LONG':([88,],[108,]),'CHAR':([88,],[109,]),'BOOLEAN':([88,],[110,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,2,3,30,92,],[1,21,22,57,113,]),'sentencia':([0,2,3,13,14,15,30,83,92,],[2,2,2,31,31,31,2,31,2,]),'function':([0,2,3,30,92,],[3,3,3,3,3,]),'asignacion':([0,2,3,13,14,15,30,83,92,],[4,4,4,4,4,4,4,4,4,]),'estructuraControl':([0,2,3,13,14,15,30,83,92,],[5,5,5,5,5,5,5,5,5,]),'bucles':([0,2,3,13,14,15,30,83,92,],[6,6,6,6,6,6,6,6,6,]),'llamada':([0,2,3,13,14,15,30,83,92,],[7,7,7,7,7,7,7,7,7,]),'declaracion':([0,2,3,13,14,15,30,83,92,],[8,8,8,8,8,8,8,8,8,]),'declarador':([0,2,3,13,14,15,30,83,92,],[11,11,11,11,11,11,11,11,11,]),'while':([0,2,3,13,14,15,30,83,92,],[14,14,14,14,14,14,14,14,14,]),'for':([0,2,3,13,14,15,30,83,92,],[15,15,15,15,15,15,15,15,15,]),'instrucciones':([13,14,15,83,],[29,33,34,99,]),'valor':([24,25,26,28,35,36,46,50,55,66,67,81,115,],[40,51,54,51,51,51,65,51,51,51,51,54,51,]),'number':([24,25,26,28,35,36,46,50,55,66,67,81,115,],[41,41,41,41,41,41,41,41,41,41,41,41,41,]),'expresion':([25,28,35,36,50,55,66,67,115,],[49,56,58,59,79,82,93,94,119,]),'args':([26,81,],[52,98,]),'params':([38,90,],[62,112,]),'operadoresMat':([49,56,58,59,79,82,93,94,119,],[66,66,66,66,66,66,66,66,66,]),'operadoresLog':([49,56,58,59,79,82,93,94,119,],[67,67,67,67,67,67,67,67,67,]),'instruccionesF':([63,89,],[91,111,]),'dato':([88,],[102,]),'retorno':([92,113,],[114,117,]),}

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
  ('retorno -> RETURN expresion','retorno',2,'p_retorno','sintactico.py',43),
  ('estructuraControl -> IF LPAREN expresion RPAREN instrucciones','estructuraControl',5,'p_estructuraControlIf','sintactico.py',48),
  ('estructuraControl -> ELSE instrucciones','estructuraControl',2,'p_estructuraControlElse','sintactico.py',51),
  ('bucles -> while instrucciones','bucles',2,'p_bucles','sintactico.py',54),
  ('bucles -> for instrucciones','bucles',2,'p_bucles','sintactico.py',55),
  ('while -> WHILE LPAREN expresion RPAREN','while',4,'p_while','sintactico.py',60),
  ('for -> FOR LPAREN ID IN ID RPAREN','for',6,'p_for','sintactico.py',64),
  ('function -> FUNCTION ID LPAREN params RPAREN instruccionesF','function',6,'p_function','sintactico.py',69),
  ('function -> FUNCTION ID LPAREN RPAREN instruccionesF','function',5,'p_function_sin_params','sintactico.py',72),
  ('llamada -> PRINTLN LPAREN expresion RPAREN','llamada',4,'p_print','sintactico.py',75),
  ('llamada -> ID LPAREN args RPAREN','llamada',4,'p_llamada_funcion','sintactico.py',80),
  ('llamada -> ID LPAREN RPAREN','llamada',3,'p_llamada_funcion_sin_params','sintactico.py',84),
  ('function -> ID LSBRACKET valor RSBRACKET','function',4,'p_index','sintactico.py',88),
  ('dato -> INT','dato',1,'p_dato','sintactico.py',93),
  ('dato -> FLOAT','dato',1,'p_dato','sintactico.py',94),
  ('dato -> BYTE','dato',1,'p_dato','sintactico.py',95),
  ('dato -> SHORT','dato',1,'p_dato','sintactico.py',96),
  ('dato -> DOUBLE','dato',1,'p_dato','sintactico.py',97),
  ('dato -> ID','dato',1,'p_dato','sintactico.py',98),
  ('dato -> LONG','dato',1,'p_dato','sintactico.py',99),
  ('dato -> CHAR','dato',1,'p_dato','sintactico.py',100),
  ('dato -> BOOLEAN','dato',1,'p_dato','sintactico.py',101),
  ('params -> ID : dato','params',3,'p_params','sintactico.py',105),
  ('params -> params , params','params',3,'p_params2','sintactico.py',109),
  ('args -> valor','args',1,'p_args','sintactico.py',113),
  ('args -> args , args','args',3,'p_args2','sintactico.py',117),
  ('valor -> ID','valor',1,'p_valor_id','sintactico.py',120),
  ('valor -> number','valor',1,'p_valor','sintactico.py',124),
  ('valor -> STRING','valor',1,'p_valor','sintactico.py',125),
  ('valor -> TRUE','valor',1,'p_valor_bool','sintactico.py',129),
  ('valor -> FALSE','valor',1,'p_valor_bool','sintactico.py',130),
  ('valor -> NULL','valor',1,'p_valor_null','sintactico.py',138),
  ('valor -> NOT valor','valor',2,'p_valor_negado','sintactico.py',143),
  ('declarador -> VAR','declarador',1,'p_declarador','sintactico.py',148),
  ('declarador -> VAL','declarador',1,'p_declarador','sintactico.py',149),
  ('asignacion -> ID ASSIGN expresion','asignacion',3,'p_asignacion','sintactico.py',153),
  ('asignacion -> declarador ID ASSIGN expresion','asignacion',4,'p_asignacion_declarando','sintactico.py',164),
  ('declaracion -> declarador ID','declaracion',2,'p_declaracion','sintactico.py',171),
  ('expresion -> LPAREN expresion RPAREN','expresion',3,'p_exresion','sintactico.py',177),
  ('expresion -> valor','expresion',1,'p_expesion','sintactico.py',180),
  ('expresion -> expresion operadoresMat expresion','expresion',3,'p_expresion_matematica','sintactico.py',185),
  ('expresion -> expresion operadoresLog expresion','expresion',3,'p_expresion_logica','sintactico.py',202),
  ('operadoresLog -> OR','operadoresLog',1,'p_operadores_log','sintactico.py',213),
  ('operadoresLog -> AND','operadoresLog',1,'p_operadores_log','sintactico.py',214),
  ('operadoresLog -> EQUALS','operadoresLog',1,'p_operadores_log','sintactico.py',215),
  ('operadoresLog -> NOTEQUALS','operadoresLog',1,'p_operadores_log','sintactico.py',216),
  ('operadoresLog -> GREATER','operadoresLog',1,'p_operadores_log','sintactico.py',217),
  ('operadoresLog -> LOWER','operadoresLog',1,'p_operadores_log','sintactico.py',218),
  ('operadoresLog -> GREATER ASSIGN','operadoresLog',2,'p_operadores_log','sintactico.py',219),
  ('operadoresLog -> LOWER ASSIGN','operadoresLog',2,'p_operadores_log','sintactico.py',220),
  ('operadoresMat -> MINUS','operadoresMat',1,'p_operadores_mat','sintactico.py',225),
  ('operadoresMat -> PLUS','operadoresMat',1,'p_operadores_mat','sintactico.py',226),
  ('operadoresMat -> TIMES','operadoresMat',1,'p_operadores_mat','sintactico.py',227),
  ('operadoresMat -> DIVIDE','operadoresMat',1,'p_operadores_mat','sintactico.py',228),
  ('operadoresMat -> MODULE','operadoresMat',1,'p_operadores_mat','sintactico.py',229),
  ('number -> INTV','number',1,'p_number','sintactico.py',237),
  ('number -> FLOATV','number',1,'p_number','sintactico.py',238),
]
