from collections import deque
queue = deque()

# queue.append("A")
# queue.append("B")
# queue.append("C")

# print("Queue after enqueuing elements: ", queue , end="")
# print("\n")

# print("Queue after dequeuing elements: ", queue.popleft())
# print("Queue after dequeuing elements: ", queue.popleft())

# print("Queue after dequeuing elements: ", queue)

class DequeByList:
    def __init__(self, size):
        self.queue = deque()
        self.size = size
    def isfull(self):
        if len(self.queue) == self.size :
            return True
        else :
            return False
    def isempty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    def Insertatlast(self):
        if self.isfull():
            print("Queue Overflow")
        else:
            try:
                element = int(input("Enter the Data: "))
                self.queue.append(element)
                print(f"Element {element} inserted at last")
            except ValueError:
                print("Please enter a valid integer!")
                
    def Insertatfront(self):
        if self.isfull():
            print("Queue Overflow")
        else:
            try:
                element = int(input("Enter the Data: "))
                self.queue.appendleft(element)
                print(f"Element {element} inserted at front")
            except ValueError:
                print("Please enter a valid integer!")
    def Dequeatlast(self):
        if self.isempty():
            print("Queue Underflow")
        else:
            removed = self.queue.pop()
            print(f"Removed element from last: {removed}")
    def Dequeatfront(self):
        if self.isempty():
            print("Queue Underflow")
        else:
            removed = self.queue.popleft()
            print(f"Removed element from front: {removed}")
    def peak(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print("Peak Element is: ",self.queue[0])
    def display(self):
        print("Queue is : ", self.queue)

    
queue_size = int(input("Enter the Size of Deque: "))
q  = DequeByList(queue_size)

while(1):
 try:
  print("\nMenu")
  print("1. Insert at Front")
  print("2. Insert at Last")
  print("3. Dequeue at Front")
  print("4. Dequeue at Last")
  print("5. Display a Peak")
  print("6. Display a Deque")
  print("7. Exit")
  choice = int(input("Enter your Choice: "))
  match(choice):
     case 1:
         q.Insertatfront()
     case 2:
         q.Insertatlast()
     case 3:
          q.Dequeatfront()
     case 4:
          q.Dequeatlast()
     case 5:
          q.peak()
     case 6:
          q.display()
     case 7:
         print("Exiting...")
         break
     case _:
         print("Invalid Input")
 except ValueError:
     print("Please enter a valid number!")
    

        
 


    
