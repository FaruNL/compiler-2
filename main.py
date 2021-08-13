from os import read
from sys import argv
from parser import parser
from semantic import variables, const, procs

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
    result = parser.parse(file_contents)
    print(f'\n\n{result}')

except FileNotFoundError as err:
    print(f'Could not open file {file_name}')

else:
    reader.close()

print(variables)
print(const)
print(procs)
