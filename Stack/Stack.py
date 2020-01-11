# stack is Last in first out data sturcutre it can be implemented using array and linked list if you implement using array then memory allocation is an issue
# in python it can be done using list, dequeue and lifoquque and direct using linked list also

"""
Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
Peek or Top: Returns top element of stack.
isEmpty: Returns true if stack is empty, else false.

"""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.root = None

    def push(self, item):
        newNode = Node(item)
        newNode.next = self.root
        self.root = newNode
    
    def pop(self):
        temp = self.root
        self.root = self.root.next
        return temp.data
    
    def peek(self):
        return self.root.data


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.peek())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    
