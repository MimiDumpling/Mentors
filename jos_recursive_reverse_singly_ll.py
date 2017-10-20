class Node(object):

    def __init__(self, data, next):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class SingleList(object):

    head = None

    def append(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def show(self):
        print "Show list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.data
            current_node = current_node.next

def reverse(sll, current_node):
    # Magic happens here
    # sll is only passed in so that you can update head when you hit the base case

    def reverse_helper(current_node, prev_node):

        if current_node is None:
            return prev_node

        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

        return reverse_helper(current_node, prev_node)

    sll.head = current_node

    # if current_node is None:
    #     sll.head = current_node
    #     return sll.head
    # else:
    #     print current_node.data
    #     print "++++++"
    #     print current_node.next.data
    #     return reverse(sll, current_node.next)


if __name__ == '__main__':
    s = SingleList()
    s.append(1)
    s.append(2)
    s.append(3)
    s.show()
    reverse(s, s.head)
    s.show()
