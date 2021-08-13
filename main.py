from sys import argv
from parser import parser

###########################
#  _____   _    _  _   _  #
# |  __ \ | |  | || \ | | #
# | |__) || |  | ||  \| | #
# |  _  / | |  | || . ` | #
# | | \ \ | |__| || |\  | #
# |_|  \_\ \____/ |_| \_| #
###########################

file_name = argv[1]
try:
    with open(file_name, 'r') as reader:
        file_contents = reader.read()
    
    print('\n~~~~~~~~~~~~~~~~~~~~~~~')
    print('Nodes order by LALR(1)')
    print('~~~~~~~~~~~~~~~~~~~~~~~\n')
    result = parser.parse(file_contents)

    print('\n~~~~~~~~~~~~~~~~~~~~~~~')
    print('Parser Tree')
    print('~~~~~~~~~~~~~~~~~~~~~~~\n')
    print(result)

except FileNotFoundError as err:
    print(f'Could not open file {file_name}')

else:
    reader.close()
