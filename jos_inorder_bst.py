class Node:
    """Makes a node in a search tree."""

    def __init__(self, data, children):

        self.data = data
        self.children = children
        self.left = None
        self.right = None

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node %s>" % self.data

    

class Tree:
    """Makes a search tree."""

    def __init__(self):

        self.root = None


    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root=%s>" % self.root

    def add(self, value):
        """Adds a node."""

        if self.root == None:
            self.root = Node(value)
        else:
            self.recurs_add(value, self.root)

    def recurs_add(self, value, node):
        if value < node.data:
            if node.left is not None:
                self.recurs_add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self.recurs_add(value, node.right)
            else:
                node.right = Node(value)

    def inorder(self, node):

        if node is not None:
            self.inorder(node.left)
            print node.data

            self.inorder(node.right)
            print node.data
