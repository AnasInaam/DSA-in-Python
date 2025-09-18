class Node:
    def __init__(self , data = 0 , next = None):
        self.data = data 
        self.next = next
class Stackll:
    def __init__(self):
        self.head = None
    def push(self):
        if self.head == None:
            self.head = Node(int(input("Enter Data: ")))
        else :
            temp = self.head
            self.head = Node(int(input("Enter Data: ")))
            self.head.next = temp
    def pop(self):
        if self.head == None:
            print("Stack is Empty")
        else:
            self.head = self.head.next
            
    def display(self):
         if self.head == None:
            print("Stack is Empty")
         else:
            temp = self.head 
            while temp != None:
                print(temp.data , end='\n')
                temp = temp.next 

    
s = Stackll()
while(1):


 print("\nMenu")
 print("1. Push")
 print("2. Pop")
 print("3. display")
 print("4. Exit")
 choice = int(input("Enter your Choice: "))
 match(choice):
    case 1:
        s.push()
    case 2:
        s.pop()
    case 3:
         s.display()
    case 4:
         exit()
    case _:
        print("Invalid Input")
    

        
            
            


            

            
