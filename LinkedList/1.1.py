"""for finding duplicate first approach iterate to loop and  maintain count in dictionary 
and if you find then remove the refrence of that loop. brute force approcah could be take head item and keep checking for all the items"""
#import IP.LinkedList.10
#from IP.LinkedList.L import LinkedList
import L

newLinkedList = L.LinkedList()
newLinkedList.insertAtStart(1)
newLinkedList.insertAtEnd(2)
newLinkedList.insertAtEnd(2)
def removeDup(n):
    dupList = []
    previous = None
    while(n is not None):
        if n.data in dupList:
            previous.next = n.next
        else:
            dupList.append(n.data)
            previous = n
        n = n.next


def removeDupWT(n):
    current = n
    while current is not None:
        runner = current
        while( runner.next is not None):
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
#removeDup(newLinkedList.head)
removeDupWT(newLinkedList.head)
newLinkedList.traverseList()
        

