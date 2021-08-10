variables = {}

class Node(object):
    def __init__(self, type, children=None, leaf=None):
        self.type = type
        if children:
            self.children = children
        else:
            self.children = []
        self.leaf = leaf

    # def __str__(self):
    #     return self.traverse(1)

    def traverse(self, i):
        s = self.type
        indent = "\n" + i*' |'
        if self.leaf != None:
            if isinstance(self.leaf, Node):
                print("Node")
                s += indent + self.leaf.traverse(i+1)
            else:
                s += indent + str(self.leaf)
        for children in self.children:
            s += indent + children.traverse(i+1)
        return s

class Program(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)

# class ConstAssignmentList(Node):
#     def __init__(self, type, children=None, leaf=None):
#         super().__init__(type, children=children, leaf=leaf)

class IdentList(Node):
    def __init__(self, type, children=None, leaf=None):
        super().__init__(type, children=children, leaf=leaf)
        self.__get_id()

    def __get_id(self):
        if self.leaf in variables.keys():
            print(f"Variable '{self.leaf}' already exits")
            exit(1)
        variables[self.leaf] = None
