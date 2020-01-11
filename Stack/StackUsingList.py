class StackUsingList():
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        self.stack.pop()


if __name__ == '__main__':
    stack = StackUsingList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())
    stack.pop()
    print(stack.peek())