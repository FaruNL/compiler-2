import ply.yacc as yacc
from lexer import tokens
import semantic as s

###################################################
#  _____          _____    _____  ______  _____   #
# |  __ \  /\    |  __ \  / ____||  ____||  __ \  #
# | |__) |/  \   | |__) || (___  | |__   | |__) | #
# |  ___// /\ \  |  _  /  \___ \ |  __|  |  _  /  #
# | |   / ____ \ | | \ \  ____) || |____ | | \ \  #
# |_|  /_/    \_\|_|  \_\|_____/ |______||_|  \_\ #
###################################################

precedence = (
    ('right',    'ID', 'CALL', 'BEGIN', 'IF', 'WHILE'),
    ('right',    'PROCEDURE'),
    ('right',    'VAR'),
    ('right',    'ASSIGN'),
    ('right',    'UPDATE'),
    ('left',     'NE'),
    ('left',     'LT', 'LTE', 'GT', 'GTE'),
    ('left',     'PLUS', 'MINUS'),
    ('left',     'TIMES', 'DIVIDE'),
    ('right',    'ODD'),
    ('left',     'LPAREN', 'RPAREN')
)


def p_program(p):
    '''program : block DOT'''
    p[0] = s.Program('<program>', [p[1]])


def p_block(p):
    '''block : constDecl varDecl procDecl statement'''
    p[0] = s.Block('<block>', [p[1], p[2], p[3], p[4]])


def p_constDecl(p):
    '''constDecl : CONST constAssignmentList SEMI
                 | empty'''
    if len(p) == 4:
        p[0] = s.ConstDecl('<constDecl1>', [p[2]])
    else:
        p[0] = s.ConstDecl('<constDecl2>', [], 'empty')


def p_constAssignmentList(p):
    '''constAssignmentList : ID ASSIGN NUMBER
                           | constAssignmentList COMMA ID ASSIGN NUMBER'''
    if len(p) == 4:
        p[0] = s.ConstAssignmentList('<constAssignmentList1>', [], [p[1], p[3]])
    else:
        p[0] = s.ConstAssignmentList('<constAssignmentList2>', [p[1]], [p[3], p[5]])


def p_varDecl(p):
    '''varDecl : VAR identList SEMI
               | empty'''
    if len(p) == 4:
        p[0] = s.VarDecl('<varDecl1>', [p[2]])
    else:
        p[0] = s.VarDecl('<varDecl2>', [], 'empty')


def p_identList(p):
    '''identList : ID
                 | identList COMMA ID'''
    if len(p) == 2:
        p[0] = s.IdentList('<identList1>', [], p[1])
    else:
        p[0] = s.IdentList('<identList2>', [p[1]], p[3])


def p_procDecl(p):
    '''procDecl : procDecl PROCEDURE ID SEMI block SEMI
                | empty'''
    if len(p) == 7:
        p[0] = s.ProcDecl('<procDecl1>', [p[1], p[5]], p[3])
    else:
        p[0] = s.ProcDecl('<procDecl2>', [], 'empty')


def p_statement(p):
    '''statement : ID UPDATE expression
                 | CALL ID
                 | BEGIN statementList END
                 | IF condition THEN statement
                 | WHILE condition DO statement
                 | empty'''
    if len(p) == 4:
        if p[2] == ':=':
            p[0] = s.Statement('<statement1>', [p[3]], p[1])
        else:
            p[0] = s.Node('<statement3>', [p[2]])

    elif len(p) == 5:
        if p[1] == 'IF':
            p[0] = s.Node('<statement4>', [p[2], p[4]])
        else:
            p[0] = s.Node('<statement5>', [p[2], p[4]])

    elif len(p) == 3:
        p[0] = s.Node('<statement2>', [], p[2])
    else:
        p[0] = s.Node('<statement>', [], 'empty')


def p_statementList(p):
    '''statementList : statement
                     | statementList SEMI statement'''
    if len(p) == 2:
        p[0] = s.StatementList('<statementList1>', [p[1]])
    else:
        p[0] = s.StatementList('<statementList2>', [p[1], p[3]])


def p_condition(p):
    '''condition : ODD expression
                 | expression relation expression'''
    if len(p) == 3:
        p[0] = s.Condition('<condition1>', [p[2]])
    else:
        p[0] = s.Condition('<condition2>', [p[1], p[2], p[3]])


def p_relation(p):
    '''relation : ASSIGN
                | NE
                | LT
                | GT
                | LTE
                | GTE'''
    if p[1] == '=':
        p[0] = s.Relation('<relation>', [], p[1])
    elif p[1] == '<>':
        p[0] = s.Relation('<relation>', [], p[1])
    elif p[1] == '<':
        p[0] = s.Relation('<relation>', [], p[1])
    elif p[1] == '>':
        p[0] = s.Relation('<relation>', [], p[1])
    elif p[1] == '<=':
        p[0] = s.Relation('<relation>', [], p[1])
    else:
        p[0] = s.Relation('<relation>', [], p[1])


def p_expression(p):
    '''expression : term
                  | addingOperator term
                  | expression addingOperator term'''
    if len(p) == 2:
        p[0] = s.Expression('<expression1>', [p[1]])
    elif len(p) == 3:
        p[0] = s.Expression('<expression2>', [p[1], p[2]])
    else:
        p[0] = s.Expression('<expression3>', [p[1], p[2], p[3]])


def p_addingOperator(p):
    '''addingOperator : PLUS
                      | MINUS'''
    if p[1] == '+':
        p[0] = s.AddingOperator('<adding_op>', [], p[1])
    else:
        p[0] = s.AddingOperator('<adding_op>', [], p[1])


def p_term(p):
    '''term : factor
            | term multiplyingOperator factor'''
    if len(p) == 2:
        p[0] = s.Term('<term1>', [p[1]])
    else:
        p[0] = s.Term('<term2>', [p[1], p[2], p[3]])


def p_multiplyingOperator(p):
    '''multiplyingOperator : TIMES
                           | DIVIDE'''
    if p[1] == '*':
        p[0] = s.MultiplyingOperator('<multiply_op>', [], p[1])
    else:
        p[0] = s.MultiplyingOperator('<multiply_op>', [], p[1])


def p_factor_ID(p):
    '''factor : ID'''
    p[0] = s.Id('<factor>', [], p[1])


def p_factor_NUMBER(p):
    '''factor : NUMBER'''
    p[0] = s.Number('<factor>', [], p[1])


def p_factor_GROUP(p):
    '''factor : LPAREN expression RPAREN'''
    p[0] = s.Group('group_expression', [p[2]])


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if p == None:
        print('Syntax error at last token')
        exit(1)
    else:
        print(f"Syntax error around line number {p.lineno} : '{p.value}'")
        exit(1)


parser = yacc.yacc()
