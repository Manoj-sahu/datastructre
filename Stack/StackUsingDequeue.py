from collections import deque

class StackUsingDequeue():
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        self.stack.append(item)
    
    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        self.stack.pop()