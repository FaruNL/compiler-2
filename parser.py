import ply.yacc as yacc
from lexer import tokens
from sys import argv

#############################################
#   _____  ______  _______  _    _  _____   #
#  / ____||  ____||__   __|| |  | ||  __ \  #
# | (___  | |__      | |   | |  | || |__) | #
#  \___ \ |  __|     | |   | |  | ||  ___/  #
#  ____) || |____    | |   | |__| || |      #
# |_____/ |______|   |_|    \____/ |_|      #
#############################################

file_name = argv[1]
with open(file_name, 'r') as reader:
    file_contents = reader.read()

###################################################
#  _____          _____    _____  ______  _____   #
# |  __ \  /\    |  __ \  / ____||  ____||  __ \  #
# | |__) |/  \   | |__) || (___  | |__   | |__) | #
# |  ___// /\ \  |  _  /  \___ \ |  __|  |  _  /  #
# | |   / ____ \ | | \ \  ____) || |____ | | \ \  #
# |_|  /_/    \_\|_|  \_\|_____/ |______||_|  \_\ #
###################################################

# def p_program(p):
#     'program : classa'
#     p[0] = p[1]

# def p_class(p):
#     'classa : CLASS typea LBRACE integera RBRACE'
#     p[0] = (p.lineno(1), 'class_noinherit', p[2], p[4])

# def p_type(p):
#     'typea : TYPE'
#     p[0] = p[1]

# def p_integer(p):
#     'integera : INTEGER'
#     p[0] = int(p[1])

def p_program(p):
    'program : classlist'
    p[0] = p[1]

def p_classlist_none(p):
    'classlist : '
    p[0] = []

def p_classlist_multi(p):
    'classlist : class SEMI classlist'
    p[0] = [p[1]] + p[3]

def p_class_noinherit(p):
    'class : CLASS type LBRACE featurelist RBRACE'
    p[0] = (p.lineno(1), 'class_no_inherit', p[2], p[4])

def p_type(p):
    'type : TYPE'
    p[0] = (p.lineno(1), p[1])

def p_identifier(p):
    'identifier : IDENTIFIER'
    p[0] = (p.lineno(1), p[1])

def p_featurelist_none(p):
    'featurelist : '
    p[0] = []

def p_featurelist_some(p):
    'featurelist : feature SEMI featurelist'
    p[0] = [p[1]] + p[3]

def p_feature_attribute_noinit(p):
    'feature : identifier COLON type'
    p[0] = (p.lineno(1),  'attribute_no_init', p[1], p[3])

def p_error(p):
    print(f"Error: {p.lineno}: Parser: cerca de '{p.value}'")

parser = yacc.yacc()

result = parser.parse(file_contents)
print(result)
