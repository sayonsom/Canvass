class Tree:
    def __call__(self):
        return Tree(self)

    def __init__(self, parent):
        self.parent = parent
        self.default_factory = self

    @property
    def arguments(self):
        return (self.value,) + self.children

    def __eq__(self, tree):
        return self.arguments == tree.arguments

    def __repr__(self):
        argumentStr = ', '.join(map(repr, self.arguments))
        return '%s(%s)' % (self.__class__.__name__, argumentStr)


t = Tree(None)
t[1][2] = 3
print t
