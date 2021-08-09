import ply.yacc as yacc
from lexer import tokens
from ast_custom import Number, BinOp, Expr, Node

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
    '''program : block'''
    p[0] = Node('program', p[1])
    print("program")


def p_block(p):
    '''block : constDecl varDecl procDecl statement'''
    p[0] = Node('block', [p[1], p[2], p[3], p[4]])
    print("block")


def p_constDecl(p):
    '''constDecl : CONST constAssignmentList SEMI
                 | empty'''
    if len(p) == 4:
        p[0] = Node('constDecl', p[2])
        print("constDecl")
    else:
        p[0] = None
        print("constDecl_nulo")
    # print "constDecl"


def p_constAssignmentList(p):
    '''constAssignmentList : ID ASSIGN NUMBER
                           | constAssignmentList COMMA ID ASSIGN NUMBER'''
    if len(p) == 4:
        print("constAssignmentList 1")
    else:
        print("constAssignmentList 2")


def p_varDecl(p):
    '''varDecl : VAR identList SEMI
               | empty'''
    if len(p) == 4:
        print("varDecl")
    else:
        print("varDecl_nulo")


def p_identList(p):
    '''identList : ID
                 | identList COMMA ID'''
    if len(p) == 2:
        print("identList 1")
    else:
        print("identList 2")


def p_procDecl(p):
    '''procDecl : procDecl PROCEDURE ID SEMI block SEMI
                | empty'''
    if len(p) == 7:
        print("procDecl")
    else:
        print("procDecl_nulo")


def p_statement(p):
    '''statement : ID UPDATE expression
                 | CALL ID
                 | BEGIN statementList END
                 | IF condition THEN statement
                 | WHILE condition DO statement
                 | empty'''
    if len(p) == 4:
        if p[2] == ':=':
            print("statement 1")
        else:
            print("statement 3")

    elif len(p) == 5:
        if p[1] == 'IF':
            print("statement 4")
        else:
            print("statement 5")
    elif len(p) == 3:
        print("statement 2")
    else:
        print("statement_nulo")


def p_statementList(p):
    '''statementList : statement
                     | statementList SEMI statement'''
    if len(p) == 2:
        print("statementList 1")
    else:
        print("statementList 2")


def p_condition(p):
    '''condition : ODD expression
                 | expression relation expression'''
    if len(p) == 2:
        print("condition 1")
    else:
        print("condition 2")


def p_relation(p):
    '''relation : ASSIGN
                | NE
                | LT
                | GT
                | LTE
                | GTE'''
    if p[1] == ':=':
        print("relation :=")
    elif p[1] == '!=':
        print("relation !=")
    elif p[1] == '<':
        print("relation <")
    elif p[1] == '>':
        print("relation >")
    elif p[1] == '<=':
        print("relation <=")
    else:
        print("relation >=")


def p_expression(p):
    '''expression : term
                  | addingOperator term
                  | expression addingOperator term'''
    if len(p) == 2:
        print("expresion 1")
    elif len(p) == 3:
        print("expresion 2")
    else:
        print("expresion 3")


def p_addingOperator(p):
    '''addingOperator : PLUS
                      | MINUS'''
    if p[1] == '+':
        print("addingOperator +")
    else:
        print("addingOperator -")


def p_term(p):
    '''term : factor
            | term multiplyingOperator factor'''
    if len(p) == 2:
        print("term 1")
    else:
        print("term 2")


def p_multiplyingOperator(p):
    '''multiplyingOperator : TIMES
                           | DIVIDE'''
    if p[1] == '*':
        print("multiplyingOperator *")
    else:
        print("multiplyingOperator /")


def p_factor_ID(p):
    '''factor : ID'''
    print("factor 1")


def p_factor_NUMBER(p):
    '''factor : NUMBER'''
    print("factor 2")


def p_factor_GROUP(p):
    '''factor : LPAREN expression RPAREN'''
    print("factor 3")


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if p:
        print(f"Error: {p.lineno}: Parser: cerca de '{p.value}'")


parser = yacc.yacc('SLR')
