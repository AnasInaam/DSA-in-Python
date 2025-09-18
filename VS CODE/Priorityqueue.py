class PriorityQueue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def insert(self, data,):
        self.queue.append(data)
        
    # def delete(self):
    #     if not self.is_empty():
    #         return self.queue.pop(0)
    #     return None
    # def peek(self):
    #     if not self.is_empty():
    #         return self.queue[0]
    #     return None
    def display(self):
       print("Priority queue: " , sorted(self.queue , reverse= False))

pq = PriorityQueue()
pq.insert(10)
pq.insert(30)
pq.insert(60)
pq.insert(20)
pq.insert(50)

pq.display()
