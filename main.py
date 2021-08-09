from os import read
from sys import argv
from parser import parser

file_name = argv[1]
try:
    with open(file_name, 'r') as reader:
        file_contents = reader.read()
    result = parser.parse(file_contents)

except FileNotFoundError as err:
    print(f'Could not open file {file_name}')

else:
    reader.close()
