from queue import LifoQueue

class StackUsingLifoQueue():
    def __init__(self):
        self.stack = LifoQueue()
    
    def push(self, item):
        self.stack.put(item)
    
    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        self.stack.get()

