class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        self.queue.pop(0)
    
    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.front())
    print(q.rear())

     

