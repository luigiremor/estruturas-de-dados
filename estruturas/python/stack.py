class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():

    def __init__(self):
        self.head = None

    def push(self, data):
        if self.empty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if not self.empty():
            popped = self.head.data
            self.head = self.head.next
            return popped
    
    def empty(self):
        return self.head == None
    
    def __iter__(self):
        current = self.head
        while current != None:
            yield current.data
            current = current.next
            