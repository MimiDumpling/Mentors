class Node(object):
 
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext
 
 
class DoubleList(object):
 
    head = None
    tail = None
 
    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
            
 
    def show(self):
        print "Show list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.data
 
            current_node = current_node.next


def reverse_recursively(node):

    # base case
    if node.next is None:
        print "*****"
        print "This is node: ", node.data
        print "This is node.prev: ", node.prev.data
        print "This is node.prev.prev: ", node.prev.prev.data
        return

    else:
        temp1 = node
        temp2 = node.prev
        node.prev = node.next
        node.next = temp2
        node = node.prev

    return reverse_recursively(node)



        # reverse_recursively(self, current.next)
        # temp = current.next
        # temp.next = current
        # current.next = None

        # call function on itself
        # use helper function to redefine self.head?

        
    # def helper(self):
    #     "Visit a node and switch the next & prev"            
 
 
d = DoubleList()
 
d.append(1)
d.append(2)
d.append(3)
d.show()

print "+++++++++++++++++++++"

reverse_recursively(d.head)
d.show()
