
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND ASSIGN BOOLEAN BYTE CHAR DIVIDE DOUBLE ELSE EQUALS FALSE FLOAT FLOATV FOR FUNCTION GREATER ID IF IN INT INTV LCBRACKET LONG LOWER LPAREN LSBRACKET MINUS MODULE NOT NOTEQUALS NULL OR PLUS PRINTLN RCBRACKET RETURN RPAREN RSBRACKET SHORT STRING TIMES TRUE VAL VAR WHILEcuerpo : sentencia  cuerpo : function  cuerpo : sentencia cuerpocuerpo : function cuerposentencia : asignacion \n                | estructuraControl\n                | bucles\n                | llamada\n                | declaracion instrucciones : LCBRACKET cuerpo RCBRACKET\n                | sentencia instruccionesF : LCBRACKET cuerpo retorno RCBRACKETinstruccionesF : LCBRACKET retorno RCBRACKETretorno : RETURN expresion estructuraControl : IF LPAREN expresion RPAREN instrucciones estructuraControl : ELSE instrucciones bucles : while instrucciones\n                | for instrucciones while : WHILE LPAREN expresion RPAREN for : FOR LPAREN ID IN ID RPAREN function : FUNCTION ID LPAREN params RPAREN instruccionesFfunction : FUNCTION ID LPAREN RPAREN instruccionesFllamada : PRINTLN LPAREN expresion RPARENllamada : ID LPAREN args RPAREN llamada : ID LPAREN RPAREN llamada : ID '.' ID LPAREN args RPARENfunction : ID LSBRACKET expresion RSBRACKETdato : INT\n            | FLOAT\n            | BYTE\n            | SHORT\n            | DOUBLE\n            | ID\n            | LONG\n            | CHAR\n            | BOOLEANparams : ID ':' dato params : params ',' paramsargs : expresionargs : args ',' argsvalor : IDvalor : number\n            | STRINGvalor : TRUE\n            | FALSEvalor : NULLvalor : NOT valor declarador : VAR\n                | VALasignacion : ID ASSIGN expresion asignacion : declarador ID ASSIGN expresion declaracion : declarador ID expresion : LPAREN expresion RPARENexpresion : valor expresion : expresion operadoresMat expresion expresion : expresion operadoresLog expresion operadoresLog :  OR\n                    | AND\n                    | EQUALS\n                    | NOTEQUALS\n                    | GREATER\n                    | LOWER\n                    | GREATER ASSIGN\n                    | LOWER ASSIGNoperadoresMat : MINUS\n                    | PLUS\n                    | TIMES\n                    | DIVIDE\n                    | MODULE number : INTV\n            | FLOATV "
    
_lr_action_items = {'FUNCTION':([0,2,3,4,5,6,7,8,28,30,31,32,34,35,40,43,44,45,46,47,48,50,51,52,54,66,81,82,85,87,88,94,95,96,97,100,103,115,120,123,125,],[9,9,9,-5,-6,-7,-8,-9,-52,-16,9,-11,-17,-18,-41,-54,-42,-43,-44,-45,-46,-70,-71,-50,-25,-27,-47,-24,-51,-10,-23,-22,9,-55,-56,-53,-15,-21,-26,-13,-12,]),'ID':([0,2,3,4,5,6,7,8,9,11,13,14,15,17,18,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,57,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,88,89,90,91,93,94,95,96,97,98,99,100,103,115,119,120,121,123,125,],[10,10,10,-5,-6,-7,-8,-9,23,28,33,33,33,-48,-49,40,40,40,56,-52,40,-16,10,-11,-17,-18,40,40,62,63,-41,40,-54,-42,-43,-44,-45,-46,40,-70,-71,-50,-25,40,-27,40,40,-65,-66,-67,-68,-69,-57,-58,-59,-60,-61,-62,-47,-24,40,40,-51,33,-10,-23,-19,104,105,63,-22,10,-55,-56,-63,-64,-53,-15,-21,40,-26,-20,-13,-12,]),'IF':([0,2,3,4,5,6,7,8,13,14,15,28,30,31,32,34,35,40,43,44,45,46,47,48,50,51,52,54,66,81,82,85,86,87,88,89,94,95,96,97,100,103,115,120,121,123,125,],[12,12,12,-5,-6,-7,-8,-9,12,12,12,-52,-16,12,-11,-17,-18,-41,-54,-42,-43,-44,-45,-46,-70,-71,-50,-25,-27,-47,-24,-51,12,-10,-23,-19,-22,12,-55,-56,-53,-15,-21,-26,-20,-13,-12,]),'ELSE':([0,2,3,4,5,6,7,8,13,14,15,28,30,31,32,34,35,40,43,44,45,46,47,48,50,51,52,54,66,81,82,85,86,87,88,89,94,95,96,97,100,103,115,120,121,123,125,],[13,13,13,-5,-6,-7,-8,-9,13,13,13,-52,-16,13,-11,-17,-18,-41,-54,-42,-43,-44,-45,-46,-70,-71,-50,-25,-27,-47,-24,-51,13,-10,-23,-19,-22,13,-55,-56,-53,-15,-21,-26,-20,-13,-12,]),'PRINTLN':([0,2,3,4,5,6,7,8,13,14,15,28,30,31,32,34,35,40,43,44,45,46,47,48,50,51,52,54,66,81,82,85,86,87,88,89,94,95,96,97,100,103,115,120,121,123,125,],[16,16,16,-5,-6,-7,-8,-9,16,16,16,-52,-16,16,-11,-17,-18,-41,-54,-42,-43,-44,-45,-46,-70,-71,-50,-25,-27,-47,-24,-51,16,-10,-23,-19,-22,16,-55,-56,-53,-15,-21,-26,-20,-13,-12,]),'VAR':([0,2,3,4,5,6,7,8,13,14,15,28,30,31,32,34,35,40,43,44,45,46,47,48,50,51,52,54,66,81,82,85,86,87,88,89,94,95,96,97,100,103,115,120,121,123,125,],[17,17,17,-5,-6,-7,-8,-9,17,17,17,-52,-16,17,-11,-17,-18,-41,-54,-42,-43,-44,-45,-46,-70,-71,-50,-25,-27,-47,-24,-51,17,-10,-23,-19,-22,17,-55,-56,-53,-15,-21,-26,-20,-13,-12,]),'VAL':([0,2,3,4,5,6,7,8,13,14,15,28,30,31,32,34,35,40,43,44,45,46,47,48,50,51,52,54,66,81,82,85,86,87,88,89,94,95,96,97,100,103,115,120,121,123,125,],[18,18,18,-5,-6,-7,-8,-9,18,18,18,-52,-16,18,-11,-17,-18,-41,-54,-42,-43,-44,-45,-46,-70,-71,-50,-25,-27,-47,-24,-51,18,-10,-23,-19,-22,18,-55,-56,-53,-15,-21,-26,-20,-13,-12,]),'WHILE':([0,2,3,4,5,6,7,8,13,14,15,28,30,31,32,34,35,40,43,44,45,46,47,48,50,51,52,54,66,81,82,85,86,87,88,89,94,95,96,97,100,103,115,120,121,123,125,],[19,19,19,-5,-6,-7,-8,-9,19,19,19,-52,-16,19,-11,-17,-18,-41,-54,-42,-43,-44,-45,-46,-70,-71,-50,-25,-27,-47,-24,-51,19,-10,-23,-19,-22,19,-55,-56,-53,-15,-21,-26,-20,-13,-12,]),'FOR':([0,2,3,4,5,6,7,8,13,14,15,28,30,31,32,34,35,40,43,44,45,46,47,48,50,51,52,54,66,81,82,85,86,87,88,89,94,95,96,97,100,103,115,120,121,123,125,],[20,20,20,-5,-6,-7,-8,-9,20,20,20,-52,-16,20,-11,-17,-18,-41,-54,-42,-43,-44,-45,-46,-70,-71,-50,-25,-27,-47,-24,-51,20,-10,-23,-19,-22,20,-55,-56,-53,-15,-21,-26,-20,-13,-12,]),'$end':([1,2,3,4,5,6,7,8,21,22,28,30,32,34,35,40,43,44,45,46,47,48,50,51,52,54,66,81,82,85,87,88,94,96,97,100,103,115,120,123,125,],[0,-1,-2,-5,-6,-7,-8,-9,-3,-4,-52,-16,-11,-17,-18,-41,-54,-42,-43,-44,-45,-46,-70,-71,-50,-25,-27,-47,-24,-51,-10,-23,-22,-55,-56,-53,-15,-21,-26,-13,-12,]),'RCBRACKET':([2,3,4,5,6,7,8,21,22,28,30,32,34,35,40,43,44,45,46,47,48,50,51,52,54,59,66,81,82,85,87,88,94,96,97,100,103,115,118,120,122,123,124,125,],[-1,-2,-5,-6,-7,-8,-9,-3,-4,-52,-16,-11,-17,-18,-41,-54,-42,-43,-44,-45,-46,-70,-71,-50,-25,87,-27,-47,-24,-51,-10,-23,-22,-55,-56,-53,-15,-21,123,-26,125,-13,-14,-12,]),'RETURN':([2,3,4,5,6,7,8,21,22,28,30,32,34,35,40,43,44,45,46,47,48,50,51,52,54,66,81,82,85,87,88,94,95,96,97,100,103,115,117,120,123,125,],[-1,-2,-5,-6,-7,-8,-9,-3,-4,-52,-16,-11,-17,-18,-41,-54,-42,-43,-44,-45,-46,-70,-71,-50,-25,-27,-47,-24,-51,-10,-23,-22,119,-55,-56,-53,-15,-21,119,-26,-13,-12,]),'LSBRACKET':([10,],[24,]),'ASSIGN':([10,28,33,78,79,],[25,57,25,98,99,]),'LPAREN':([10,12,16,19,20,23,24,25,26,29,33,36,37,42,56,57,67,68,69,70,71,72,73,74,75,76,77,78,79,83,84,98,99,119,],[26,29,36,37,38,39,42,42,42,42,26,42,42,42,84,42,42,42,-65,-66,-67,-68,-69,-57,-58,-59,-60,-61,-62,42,42,-63,-64,42,]),'.':([10,33,],[27,27,]),'LCBRACKET':([13,14,15,65,86,89,92,121,],[31,31,31,95,31,-19,95,-20,]),'STRING':([24,25,26,29,36,37,42,49,57,67,68,69,70,71,72,73,74,75,76,77,78,79,83,84,98,99,119,],[45,45,45,45,45,45,45,45,45,45,45,-65,-66,-67,-68,-69,-57,-58,-59,-60,-61,-62,45,45,-63,-64,45,]),'TRUE':([24,25,26,29,36,37,42,49,57,67,68,69,70,71,72,73,74,75,76,77,78,79,83,84,98,99,119,],[46,46,46,46,46,46,46,46,46,46,46,-65,-66,-67,-68,-69,-57,-58,-59,-60,-61,-62,46,46,-63,-64,46,]),'FALSE':([24,25,26,29,36,37,42,49,57,67,68,69,70,71,72,73,74,75,76,77,78,79,83,84,98,99,119,],[47,47,47,47,47,47,47,47,47,47,47,-65,-66,-67,-68,-69,-57,-58,-59,-60,-61,-62,47,47,-63,-64,47,]),'NULL':([24,25,26,29,36,37,42,49,57,67,68,69,70,71,72,73,74,75,76,77,78,79,83,84,98,99,119,],[48,48,48,48,48,48,48,48,48,48,48,-65,-66,-67,-68,-69,-57,-58,-59,-60,-61,-62,48,48,-63,-64,48,]),'NOT':([24,25,26,29,36,37,42,49,57,67,68,69,70,71,72,73,74,75,76,77,78,79,83,84,98,99,119,],[49,49,49,49,49,49,49,49,49,49,49,-65,-66,-67,-68,-69,-57,-58,-59,-60,-61,-62,49,49,-63,-64,49,]),'INTV':([24,25,26,29,36,37,42,49,57,67,68,69,70,71,72,73,74,75,76,77,78,79,83,84,98,99,119,],[50,50,50,50,50,50,50,50,50,50,50,-65,-66,-67,-68,-69,-57,-58,-59,-60,-61,-62,50,50,-63,-64,50,]),'FLOATV':([24,25,26,29,36,37,42,49,57,67,68,69,70,71,72,73,74,75,76,77,78,79,83,84,98,99,119,],[51,51,51,51,51,51,51,51,51,51,51,-65,-66,-67,-68,-69,-57,-58,-59,-60,-61,-62,51,51,-63,-64,51,]),'RPAREN':([26,39,40,43,44,45,46,47,48,50,51,53,55,58,60,61,64,80,81,96,97,100,101,102,104,105,106,107,108,109,110,111,112,113,114,116,],[54,65,-41,-54,-42,-43,-44,-45,-46,-70,-71,82,-39,86,88,89,92,100,-47,-55,-56,-53,-40,120,121,-33,-37,-28,-29,-30,-31,-32,-34,-35,-36,-38,]),'RSBRACKET':([40,41,43,44,45,46,47,48,50,51,81,96,97,100,],[-41,66,-54,-42,-43,-44,-45,-46,-70,-71,-47,-55,-56,-53,]),'MINUS':([40,41,43,44,45,46,47,48,50,51,52,55,58,60,61,80,81,85,96,97,100,124,],[-41,69,-54,-42,-43,-44,-45,-46,-70,-71,69,69,69,69,69,69,-47,69,69,69,-53,69,]),'PLUS':([40,41,43,44,45,46,47,48,50,51,52,55,58,60,61,80,81,85,96,97,100,124,],[-41,70,-54,-42,-43,-44,-45,-46,-70,-71,70,70,70,70,70,70,-47,70,70,70,-53,70,]),'TIMES':([40,41,43,44,45,46,47,48,50,51,52,55,58,60,61,80,81,85,96,97,100,124,],[-41,71,-54,-42,-43,-44,-45,-46,-70,-71,71,71,71,71,71,71,-47,71,71,71,-53,71,]),'DIVIDE':([40,41,43,44,45,46,47,48,50,51,52,55,58,60,61,80,81,85,96,97,100,124,],[-41,72,-54,-42,-43,-44,-45,-46,-70,-71,72,72,72,72,72,72,-47,72,72,72,-53,72,]),'MODULE':([40,41,43,44,45,46,47,48,50,51,52,55,58,60,61,80,81,85,96,97,100,124,],[-41,73,-54,-42,-43,-44,-45,-46,-70,-71,73,73,73,73,73,73,-47,73,73,73,-53,73,]),'OR':([40,41,43,44,45,46,47,48,50,51,52,55,58,60,61,80,81,85,96,97,100,124,],[-41,74,-54,-42,-43,-44,-45,-46,-70,-71,74,74,74,74,74,74,-47,74,74,74,-53,74,]),'AND':([40,41,43,44,45,46,47,48,50,51,52,55,58,60,61,80,81,85,96,97,100,124,],[-41,75,-54,-42,-43,-44,-45,-46,-70,-71,75,75,75,75,75,75,-47,75,75,75,-53,75,]),'EQUALS':([40,41,43,44,45,46,47,48,50,51,52,55,58,60,61,80,81,85,96,97,100,124,],[-41,76,-54,-42,-43,-44,-45,-46,-70,-71,76,76,76,76,76,76,-47,76,76,76,-53,76,]),'NOTEQUALS':([40,41,43,44,45,46,47,48,50,51,52,55,58,60,61,80,81,85,96,97,100,124,],[-41,77,-54,-42,-43,-44,-45,-46,-70,-71,77,77,77,77,77,77,-47,77,77,77,-53,77,]),'GREATER':([40,41,43,44,45,46,47,48,50,51,52,55,58,60,61,80,81,85,96,97,100,124,],[-41,78,-54,-42,-43,-44,-45,-46,-70,-71,78,78,78,78,78,78,-47,78,78,78,-53,78,]),'LOWER':([40,41,43,44,45,46,47,48,50,51,52,55,58,60,61,80,81,85,96,97,100,124,],[-41,79,-54,-42,-43,-44,-45,-46,-70,-71,79,79,79,79,79,79,-47,79,79,79,-53,79,]),',':([40,43,44,45,46,47,48,50,51,53,55,64,81,96,97,100,101,102,105,106,107,108,109,110,111,112,113,114,116,],[-41,-54,-42,-43,-44,-45,-46,-70,-71,83,-39,93,-47,-55,-56,-53,83,83,-33,-37,-28,-29,-30,-31,-32,-34,-35,-36,93,]),'IN':([62,],[90,]),':':([63,],[91,]),'INT':([91,],[107,]),'FLOAT':([91,],[108,]),'BYTE':([91,],[109,]),'SHORT':([91,],[110,]),'DOUBLE':([91,],[111,]),'LONG':([91,],[112,]),'CHAR':([91,],[113,]),'BOOLEAN':([91,],[114,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,2,3,31,95,],[1,21,22,59,117,]),'sentencia':([0,2,3,13,14,15,31,86,95,],[2,2,2,32,32,32,2,32,2,]),'function':([0,2,3,31,95,],[3,3,3,3,3,]),'asignacion':([0,2,3,13,14,15,31,86,95,],[4,4,4,4,4,4,4,4,4,]),'estructuraControl':([0,2,3,13,14,15,31,86,95,],[5,5,5,5,5,5,5,5,5,]),'bucles':([0,2,3,13,14,15,31,86,95,],[6,6,6,6,6,6,6,6,6,]),'llamada':([0,2,3,13,14,15,31,86,95,],[7,7,7,7,7,7,7,7,7,]),'declaracion':([0,2,3,13,14,15,31,86,95,],[8,8,8,8,8,8,8,8,8,]),'declarador':([0,2,3,13,14,15,31,86,95,],[11,11,11,11,11,11,11,11,11,]),'while':([0,2,3,13,14,15,31,86,95,],[14,14,14,14,14,14,14,14,14,]),'for':([0,2,3,13,14,15,31,86,95,],[15,15,15,15,15,15,15,15,15,]),'instrucciones':([13,14,15,86,],[30,34,35,103,]),'expresion':([24,25,26,29,36,37,42,57,67,68,83,84,119,],[41,52,55,58,60,61,80,85,96,97,55,55,124,]),'valor':([24,25,26,29,36,37,42,49,57,67,68,83,84,119,],[43,43,43,43,43,43,43,81,43,43,43,43,43,43,]),'number':([24,25,26,29,36,37,42,49,57,67,68,83,84,119,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'args':([26,83,84,],[53,101,102,]),'params':([39,93,],[64,116,]),'operadoresMat':([41,52,55,58,60,61,80,85,96,97,124,],[67,67,67,67,67,67,67,67,67,67,67,]),'operadoresLog':([41,52,55,58,60,61,80,85,96,97,124,],[68,68,68,68,68,68,68,68,68,68,68,]),'instruccionesF':([65,92,],[94,115,]),'dato':([91,],[106,]),'retorno':([95,117,],[118,122,]),}

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
  ('llamada -> ID . ID LPAREN args RPAREN','llamada',6,'p_llamada_objeto','sintactico.py',88),
  ('function -> ID LSBRACKET expresion RSBRACKET','function',4,'p_index','sintactico.py',92),
  ('dato -> INT','dato',1,'p_dato','sintactico.py',97),
  ('dato -> FLOAT','dato',1,'p_dato','sintactico.py',98),
  ('dato -> BYTE','dato',1,'p_dato','sintactico.py',99),
  ('dato -> SHORT','dato',1,'p_dato','sintactico.py',100),
  ('dato -> DOUBLE','dato',1,'p_dato','sintactico.py',101),
  ('dato -> ID','dato',1,'p_dato','sintactico.py',102),
  ('dato -> LONG','dato',1,'p_dato','sintactico.py',103),
  ('dato -> CHAR','dato',1,'p_dato','sintactico.py',104),
  ('dato -> BOOLEAN','dato',1,'p_dato','sintactico.py',105),
  ('params -> ID : dato','params',3,'p_params','sintactico.py',109),
  ('params -> params , params','params',3,'p_params2','sintactico.py',113),
  ('args -> expresion','args',1,'p_args','sintactico.py',117),
  ('args -> args , args','args',3,'p_args2','sintactico.py',121),
  ('valor -> ID','valor',1,'p_valor_id','sintactico.py',126),
  ('valor -> number','valor',1,'p_valor','sintactico.py',130),
  ('valor -> STRING','valor',1,'p_valor','sintactico.py',131),
  ('valor -> TRUE','valor',1,'p_valor_bool','sintactico.py',135),
  ('valor -> FALSE','valor',1,'p_valor_bool','sintactico.py',136),
  ('valor -> NULL','valor',1,'p_valor_null','sintactico.py',144),
  ('valor -> NOT valor','valor',2,'p_valor_negado','sintactico.py',149),
  ('declarador -> VAR','declarador',1,'p_declarador','sintactico.py',154),
  ('declarador -> VAL','declarador',1,'p_declarador','sintactico.py',155),
  ('asignacion -> ID ASSIGN expresion','asignacion',3,'p_asignacion','sintactico.py',159),
  ('asignacion -> declarador ID ASSIGN expresion','asignacion',4,'p_asignacion_declarando','sintactico.py',170),
  ('declaracion -> declarador ID','declaracion',2,'p_declaracion','sintactico.py',177),
  ('expresion -> LPAREN expresion RPAREN','expresion',3,'p_exresion','sintactico.py',183),
  ('expresion -> valor','expresion',1,'p_expesion','sintactico.py',187),
  ('expresion -> expresion operadoresMat expresion','expresion',3,'p_expresion_matematica','sintactico.py',192),
  ('expresion -> expresion operadoresLog expresion','expresion',3,'p_expresion_logica','sintactico.py',209),
  ('operadoresLog -> OR','operadoresLog',1,'p_operadores_log','sintactico.py',220),
  ('operadoresLog -> AND','operadoresLog',1,'p_operadores_log','sintactico.py',221),
  ('operadoresLog -> EQUALS','operadoresLog',1,'p_operadores_log','sintactico.py',222),
  ('operadoresLog -> NOTEQUALS','operadoresLog',1,'p_operadores_log','sintactico.py',223),
  ('operadoresLog -> GREATER','operadoresLog',1,'p_operadores_log','sintactico.py',224),
  ('operadoresLog -> LOWER','operadoresLog',1,'p_operadores_log','sintactico.py',225),
  ('operadoresLog -> GREATER ASSIGN','operadoresLog',2,'p_operadores_log','sintactico.py',226),
  ('operadoresLog -> LOWER ASSIGN','operadoresLog',2,'p_operadores_log','sintactico.py',227),
  ('operadoresMat -> MINUS','operadoresMat',1,'p_operadores_mat','sintactico.py',232),
  ('operadoresMat -> PLUS','operadoresMat',1,'p_operadores_mat','sintactico.py',233),
  ('operadoresMat -> TIMES','operadoresMat',1,'p_operadores_mat','sintactico.py',234),
  ('operadoresMat -> DIVIDE','operadoresMat',1,'p_operadores_mat','sintactico.py',235),
  ('operadoresMat -> MODULE','operadoresMat',1,'p_operadores_mat','sintactico.py',236),
  ('number -> INTV','number',1,'p_number','sintactico.py',244),
  ('number -> FLOATV','number',1,'p_number','sintactico.py',245),
]
