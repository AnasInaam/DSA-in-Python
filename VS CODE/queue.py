class Node:
    def __init__(self , data = 0 , next = None):
        self.data = data 
        self.next = next
class Q:
    def __init__(self):
        self.head = None
    def inqueue1(self):
        if self.head == None:
            self.head = Node(int(input("Enter Data: ")))
        else :
            temp = self.head 
            while temp.next != None:
                temp = temp.next
            temp.next = Node(int(input("Enter Data: ")))
    def dequeue1(self):
        if self.head == None:
            print("Queue is Empty")
        else :
            self.head = self.head.next
    def display(self):
         if self.head == None:
            print("Stack is Empty")
         else:
            temp = self.head 
            while temp != None:
                print(temp.data , end='-->')
                temp = temp.next 

q = Q()
while(1):
 print("\nMenu")
 print("1. Inqueue")
 print("2. Dequeue")
 print("3. display")
 print("4. Exit")
 choice = int(input("Enter your Choice: "))
 match(choice):
    case 1:
        q.inqueue1()
    case 2:
        q.dequeue1()
    case 3:
         q.display()
    case 4:
         exit()
    case _:
        print("Invalid Input")
    

        
            
            


            

            


