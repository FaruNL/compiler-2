sym_table = {}


class Node(object):
    def __init__(self, type, children=None, leaf=None):
        self.type = type
        if children:
            self.children = children
        else:
            self.children = []
        self.leaf = leaf

    def __str__(self):
        return self.__traverse_tree(1)

    def __traverse_tree(self, i):
        s = self.type
        indent = "\n" + i*' |'
        if self.leaf != None:
            s += indent + str(self.leaf)
        for children in self.children:
            s += indent + children.__traverse_tree(i+1)
        return s

    def traverse(self):
        child = None
        if self.leaf != None:
            child = self.leaf
        for children in self.children:
            child = children.traverse()
        return child


class Terminal(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class Program(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class Block(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class ConstDecl(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class ConstAssignmentList(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)
        self.__check()

    def __check(self):
        id = self.leaf[0]
        if id in sym_table.keys():
            print(f"Constant '{id}' already exits")
            exit(1)
        sym_table[id] = 'CONST'


class VarDecl(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class IdentList(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)
        self.__check()

    def __check(self):
        id = self.leaf
        if id in sym_table.keys():
            print(f"Variable '{id}' already exits")
            exit(1)
        sym_table[id] = 'VAR'


class ProcDecl(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)
        self.__check()

    def __check(self):
        id = self.leaf
        if len(self.children) == 2:

            if id in sym_table.keys():
                print(f"Procedure '{id}' is already defined")
                exit(1)
            sym_table[id] = 'PROC'


class Statement(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)
        self.__check()

    def __check(self):
        if len(self.children) == 1 and self.leaf:
            id = self.leaf
            expression = self.children[0]
            self.__check_CONST(id)
            self.__check_PROC(id)
            self.__check_VAR(id)

    def __check_CONST(self, id):
        if id in sym_table.keys():
            if sym_table[id] == 'CONST':
                print(f"You can't modify a const: '{id}'")
                exit(1)

    def __check_PROC(self, id):
        if id in sym_table.keys():
            if sym_table[id] == 'PROC':
                print(
                    f"You can't assign something to a procedure identifier: '{id}'")
                exit(1)

    def __check_VAR(self, id):
        if not id in sym_table.keys():
            print(f"'{id}' is not declared")
            exit(1)

    def __chek_expression(self, expression):
        # if expression.type == '<expression1>':
        #     print(expression)
        #     exit(0)
        pass


class StatementList(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class Condition(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class Relation(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class Expression(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class AddingOperator(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class Term(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class MultiplyingOperator(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class Id(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class Number(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class Group(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)
