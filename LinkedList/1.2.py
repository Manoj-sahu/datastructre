""" look for item if found start printing from there take one varaible make it true
"""
import L

def printElementsFromK(n, k):
    isFound = False
    while n is not None:
        if n.data == k:
            isFound = True
        if isFound:
            print(n.data)
        n = n.next

newLinkedList = L.LinkedList()
newLinkedList.insertAtStart(1)
newLinkedList.insertAtEnd(2)
newLinkedList.insertAtEnd(3)
newLinkedList.insertAtEnd(4)
newLinkedList.insertAtEnd(5)

printElementsFromK(newLinkedList.head, 4)
