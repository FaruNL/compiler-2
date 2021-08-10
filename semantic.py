variables = {}


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


class Statement(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)
        self.__get_id_value()

    def __get_id_value(self):
        # value = str(self.children[0])
        # if value.isdigit():
            # variables[self.leaf] = int(value)
        # variables[self.leaf] = value
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


# def __str__(self):
#         return self.__print_last_child(1)


# def __print_last_child(self, i):
#         s = self.type
#         if self.leaf != None:
#             if isinstance(self.leaf, Node):
#                 print("Node")
#                 s = self.leaf.__print_last_child(i+1)
#             else:
#                 s = str(self.leaf)
#         for children in self.children:
#             s = children.__print_last_child(i+1)
#         return s
