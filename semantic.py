variables = {}
const = {}
procs = {}


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
            if isinstance(self.leaf, Node):
                print("Node")
                s += indent + self.leaf.__traverse_tree(i+1)
            else:
                s += indent + str(self.leaf)
        for children in self.children:
            s += indent + children.__traverse_tree(i+1)
        return s


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
        self.__get_const()

    def __get_const(self):
        if self.leaf[0] in const.keys():
            print(f"Constant '{self.leaf[0]}' already exits")
            exit(1)
        const[self.leaf[0]] = None


class VarDecl(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)


class IdentList(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)
        self.__get_id()

    def __get_id(self):
        if self.leaf in variables.keys():
            print(f"Variable '{self.leaf}' already exits")
            exit(1)
        variables[self.leaf] = None


class ProcDecl(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)
        self.__check_procs()

    def __check_procs(self):
        if len(self.children) == 2:
            if self.leaf in procs.keys():
                print(f"Procedure '{self.leaf}' already exits")
                exit(1)
            procs[self.leaf] = None


class Statement(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)
        self.__get_id_value()

    def __get_id_value(self):
        if len(self.children) == 1 and len(self.leaf) == 1:
            id = self.leaf
            if id in const.keys():
                print(f"No puedes modificar la constante {id}")
                exit(1)

            if not id in variables.keys():
                print(f" '{id}' no esta declarada")
                exit(1)

            # if self.children
            # valor_der = self.children[0].children[0].children[0].leaf
            # if not valor_der in variables.keys() and not valor_der in const.keys():
            #     print(f"{valor_der} no está declarada")
            #     exit(1)


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
