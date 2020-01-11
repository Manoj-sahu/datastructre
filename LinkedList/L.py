class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def traverseList(self):
        if self.head is None:
            print('list is empty')
            return
        else:
            node = self.head
            while node is not None:
                print(node.data, '')
                node = node.next
    
    def insertAtStart(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = newNode
    
    def insertAfterGivenItem(self, item, newItem):
        n = self.head
        while n is not None:
            if n.data == item:
                break
            n = n.next
        if n is None:
            print('item is not found in the list')
        else:
            newNode = Node(newItem)
            newNode.next = n.next
            n.next = newNode
    
    def insertBeforeGivenItem(self, item, newItem):
        prevNode = self.head
        while prevNode.next is not None:
            if prevNode.next.data == item:
                break
            prevNode = prevNode.next
        if prevNode.next is None:
            print('item is not found in the list')
        else:
            newNode = Node(newItem)
            newNode.next = prevNode.next
            prevNode.next = newNode
            #print('hi')
        
    def insertAtIndex(self, index, data):
        
        if index == 1:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        i = 1
        prevNode = self.head
        while i < index -1 and prevNode is not None:
            prevNode = prevNode.next
            i += 1

        if prevNode is None:
            print('Index out of bound')
        else:
            newNode = Node(data)
            newNode.next = prevNode.next
            prevNode.next = newNode
    
    def getCount(self):
        if self.head is None:
            print('0')
            return
        n = self.head
        count = 0
        while n is not None:
            count += 1
            n = n.next
        print(count)
    
    def searchItem(self, item):
        if self.head is None:
            print('List is empty')
            return False
        n = self.head
        while n is not None:
            if n.data == item:
                print('item is found')
                return True
            n = n.next
        print('Element is not found')
        return False
    
    def deleteItemFromStart(self):
        if self.head is None:
            print('list has no element')
        self.head = self.head.next
    
    def deleteItemFromEnd(self):
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None
    
    def deleteGivenItem(self, item):
        if self.head is None:
            print('list is empty')
            return
        if self.head.data == item:
            self.head = self.head.next
            return
        
        n = self.head
        while n.next is not None:
            if n.next.data == item:
                break
            n = n.next 
        
        if n.next is None:
            print('item is not found in the list')
        n.next = n.next.next
    
    def reverseLinkedList(self):
        prev = None
        n = self.head
        while n is not None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        self.head = prev

if __name__ == '__main__':
        
    newLinkedList = LinkedList()
    newLinkedList.insertAtStart(1)
    newLinkedList.insertAtEnd(2)
    newLinkedList.insertAtEnd(5)
    newLinkedList.insertAtIndex(3, 3)
    newLinkedList.insertBeforeGivenItem(5, 4)
    newLinkedList.traverseList()
    #newLinkedList.getCount()
    newLinkedList.searchItem(22)
    newLinkedList.deleteItemFromEnd()
    newLinkedList.traverseList()
    # newLinkedList.deleteItemFromStart()
    # newLinkedList.traverseList()
    # newLinkedList.deleteGivenItem(3)
    # print('after 3 delete')
    # newLinkedList.traverseList()
    newLinkedList.reverseLinkedList()
    newLinkedList.traverseList()
        


        
    


