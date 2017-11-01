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

    def find(self, data):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)


class SearchTree:
    """Makes a search tree."""

    def __init__(self):

        self.root = None


    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root=%s>" % self.root

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.find(data)




