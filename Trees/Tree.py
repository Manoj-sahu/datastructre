class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)


    def _insert(self, data, currentNode):
        #if given data has higher value than node then insert in left else right
            if currentNode.data > data:
                if currentNode.left is None:
                    currentNode.left = Node(data)
                else:
                    self.insert(data, currentNode.left)
            else:
                if currentNode.right is None:
                    currentNode.right = Node(data)
                else:
                    self._insert(data, currentNode.right)

t = Tree()
t.insert(1)
t.insert(2)
t.insert(4)
t.insert(3)


        
    

        