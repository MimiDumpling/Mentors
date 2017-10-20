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

    head = current_node
    next = current_node.next

    if next is None:
        sll.head = head
        return head
    else:
        return reverse(head.next)


if __name__ == '__main__':
    s = SingleList()
    s.append(1)
    s.append(2)
    s.append(3)
    s.show()
    reverse(s, s.head)
    s.show()
