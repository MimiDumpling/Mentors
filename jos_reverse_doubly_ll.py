class Node(object):
 
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
 
 
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
 
 
    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp

        if current is None:
            current.prev = self.head
            
 
    def show(self):
        print "Show list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.prev.data if hasattr(current_node.prev, "data") else None,
            print current_node.data,
            print current_node.next.data if hasattr(current_node.next, "data") else None
 
            current_node = current_node.next
            print "*"*50
 
 
d = DoubleList()
 
d.append("a")
d.show()
d.append("b")
d.show()

print "+++++++++++++++++++++"

d.reverse()
d.show()












