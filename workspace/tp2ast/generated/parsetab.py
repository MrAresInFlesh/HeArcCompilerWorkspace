
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftADD_OPleftMUL_OPrightUNARY_MINUSADD_OP IDENTIFIER MUL_OP NUMBERprogramme : statementprogramme : statement ';' programmestatement : assignation\n    | expressionexpression : expression ADD_OP expression\n    | expression MUL_OP expressionexpression : NUMBER\n    | IDENTIFIERexpression : '(' expression ')'expression : ADD_OP expression %prec UNARY_MINUSassignation : IDENTIFIER '=' expression"
    
_lr_action_items = {'IDENTIFIER':([0,6,8,9,10,11,12,],[5,14,14,5,14,14,14,]),'NUMBER':([0,6,8,9,10,11,12,],[7,7,7,7,7,7,7,]),'(':([0,6,8,9,10,11,12,],[8,8,8,8,8,8,8,]),'ADD_OP':([0,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,],[6,10,-8,6,-7,6,6,6,6,6,-10,-8,10,-5,-6,10,-9,]),'$end':([1,2,3,4,5,7,13,14,16,17,18,19,20,],[0,-1,-3,-4,-8,-7,-10,-8,-2,-5,-6,-11,-9,]),';':([2,3,4,5,7,13,14,17,18,19,20,],[9,-3,-4,-8,-7,-10,-8,-5,-6,-11,-9,]),'MUL_OP':([4,5,7,13,14,15,17,18,19,20,],[11,-8,-7,-10,-8,11,11,-6,11,-9,]),'=':([5,],[12,]),')':([7,13,14,15,17,18,20,],[-7,-10,-8,20,-5,-6,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programme':([0,9,],[1,16,]),'statement':([0,9,],[2,2,]),'assignation':([0,9,],[3,3,]),'expression':([0,6,8,9,10,11,12,],[4,13,15,4,17,18,19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_programme_statement','parser4AST.py',16),
  ('programme -> statement ; programme','programme',3,'p_programme_recursive','parser4AST.py',21),
  ('statement -> assignation','statement',1,'p_statement','parser4AST.py',26),
  ('statement -> expression','statement',1,'p_statement','parser4AST.py',27),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','parser4AST.py',32),
  ('expression -> expression MUL_OP expression','expression',3,'p_expression_op','parser4AST.py',33),
  ('expression -> NUMBER','expression',1,'p_expression_num','parser4AST.py',38),
  ('expression -> IDENTIFIER','expression',1,'p_expression_num','parser4AST.py',39),
  ('expression -> ( expression )','expression',3,'p_expression_paren','parser4AST.py',44),
  ('expression -> ADD_OP expression','expression',2,'p_minus','parser4AST.py',49),
  ('assignation -> IDENTIFIER = expression','assignation',3,'p_assignation','parser4AST.py',54),
]
