class queueop:
    def __init__(self  , queue , size):
        self.queue = queue
        self.size = size
    def isempty(self):
        if len(queue) == 0:
            return True 
        else :
            return False
    def isfull(self):
        if len(queue) == self.size :
            return True
        else :
            return False
    def inqueue(self):
        if self.isfull():
            print("Queue is Full")
        else :
            element = int(input("Enter the Data: "))
            self.queue.append(element)
    def dequeue(self):
        if self.isempty():
            print("Queue Underflow")
        else :
            self.queue.pop(0)
    def peak(self):
        print("Peak Element is: ",self.queue[-1])
    def display(self):
        print("Stack is : ", self.queue)

  
queue= []
size = int(input("Enter the size: "))
q  = queueop(queue , size)

while(1):
 print("\nMenu")
 print("1. Enqueue an Element")
 print("2. Dequeue an Element")
 print("3. Display a Peak")
 print("4. Display a Queue")
 choice = int(input("Enter your Choice: "))
 match(choice):
    case 1:
        q.inqueue()
    case 2:
        q.dequeue()
    case 3:
         q.peak()
    case 4:
         q.display()
    case _:
        print("Invalid Input")
    

        
 

