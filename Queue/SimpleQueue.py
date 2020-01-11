class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue():
    def __init__(self):
        self.first = None
        self.last = None
    
     def add(self, item):
         newNode = Node(data)

        if self.last is not None:
            #add new node to current last
            self.last.next = newNode
        #make new node to last node
        self.last = newNode
        if self.first is None:
            self.first = self.last
    
    def remove(self):
        self.first = self.first.next
        if self.first is None:
            self.last = None

        

         self.first = newNode
         se