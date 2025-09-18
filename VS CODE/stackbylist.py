class stackoperation:
    def __init__(self , stack , size = 0):
        self.stack = stack
        self.size = size
    def isfull(self):
        if len(stack) == self.size :
            return True
        else :
            return False
    def push(self):
        if self.isfull():
            print("Stack Overflow")
        else:
            element = int(input("Enter the Data: "))
            self.stack.append(element)
    def isempty(self):
        if len(stack) == 0:
            return True 
        else :
            return False
    def pop(self):
        if self.isempty():
            print("Stack Underflow")
        else :
            self.stack.pop()
    def peak(self):
        print("Peak Element is: ",self.stack[-1])
    def display(self):
        print("Stack is : ", self.stack)

    
    
stack= []
size = int(input("Enter the size: "))
s  = stackoperation(stack , size)

while(1):
 print("\nMenu")
 print("1. Push an Element")
 print("2. Pop an Element")
 print("4. Display a Peak")
 print("3. Display a Stack")
 choice = int(input("Enter your Choice: "))
 match(choice):
    case 1:
        s.push()
    case 2:
        s.pop()
    case 3:
         s.peak()
    case 4:
         s.display()
    case _:
        print("Invalid Input")
    

        
 

