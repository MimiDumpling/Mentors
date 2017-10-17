class Node(object):
 
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
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

 
    # def reverse(self):
    #     temp = None
    #     current = self.head

    #     while current is not None:
    #         temp = current.prev
    #         current.prev = current.next
    #         current.next = temp
    #         self.head = current
    #         current = current.prev

    def reverse_recursively(self):

        current = self.head

        if self.head is None:
            return "List is empty."

        # base case
        if current.next is None:
            self.head = current
            return

        else:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            self.head = current
            current = current.prev

        if current.prev is None:
            return
        else:
            reverse_recursively()



        # reverse_recursively(self, current.next)
        # temp = current.next
        # temp.next = current
        # current.next = None

        # call function on itself
        # use helper function to redefine self.head?

    # def helper(self):
    #     "Visit a node and switch the next & prev"
            
 
    def show(self):
        print "Show list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.data
 
            current_node = current_node.next
            
 
 
d = DoubleList()
 
d.append(1)
d.append(2)
d.append(3)
d.show()

print "+++++++++++++++++++++"

d.reverse_recursively()
d.show()












