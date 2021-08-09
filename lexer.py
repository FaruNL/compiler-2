import ply.lex as lex
from re import findall

###########################################
#  _       ______ __   __ ______  _____   #
# | |     |  ____|\ \ / /|  ____||  __ \  #
# | |     | |__    \ V / | |__   | |__) | #
# | |     |  __|    > <  |  __|  |  _  /  #
# | |____ | |____  / . \ | |____ | | \ \  #
# |______||______|/_/ \_\|______||_|  \_\ #
###########################################

valid = True

#--------#
# TOKENS #
#--------#

reserved = {
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'then': 'THEN',
    'while': 'WHILE',
    'do': 'DO',
    'call': 'CALL',
    'const': 'CONST',
    'var': 'VAR',
    'procedure': 'PROCEDURE',
    'odd': 'ODD'  # ,
    # 'out': 'OUT',
    # 'in': 'IN',
    # 'else': 'ELSE'
}

tokens = [
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ASSIGN',
    'NE',
    'LT',
    'LTE',
    'GT',
    'GTE',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'SEMI',
    'DOT',
    'UPDATE'
]

tokens += reserved.values()

#---------#
# LEXEMES #
#---------#

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMI = r';'
t_DOT = r'\.'
t_UPDATE = r':='


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved.values():
        t.value = t.value.upper()
        t.type = t.value
    return t


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

# def t_STRING(t):
#     r'"[^"]*"'
#     t.value = t.value[1:-1]
#     return t

#-----------#
# OMISSIONS #
#-----------#


def t_SINGLE_LINE_COMMENT(t):
    r'\#.*'
    pass


def t_MULTI_LINE_COMMENT(t):
    r'\/\*(.|\n)*?\*\/'
    t.lexer.lineno += len(findall("\n", t.value))
    pass


t_ignore = ' \t'

#--------#
# OTHERS #
#--------#


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#----------------#
# ERROR HANDLING #
#----------------#


def t_error(t):
    print(f"ERROR: Caracter inválido '{t.value[0]}', LINEA: {t.lexer.lineno}")
    valid = False
    t.lexer.skip(1)


#-----#
# USE #
#-----#
lexer = lex.lex()

# for tok in lexer:
#     print(tok)
