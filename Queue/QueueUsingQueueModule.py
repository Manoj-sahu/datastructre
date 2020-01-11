from Queue import Queue

class QUsingQueue():
    def __init__(self):
        self.q = Queue()
    
    def enque(self, item):
        self.q.put(item)
    
    def dequeue(self):
        self.q.get()
    
    def front(self):
        return self.q[0]
    
    def rear(self):
        return self.q[-1]

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.front())
    print(q.rear())
