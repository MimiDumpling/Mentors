"""
Binary Tree Search: Breadth first 
hint: no recursion
"""

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def bfs_traverse(root):

    q = []
    q.append(root)

    while q is not []:
        current = q.pop(0)

        if current.left is not None:
            q.append(current.left)
        if current.right is not None:
            q.append(current.right)

        print current.data
