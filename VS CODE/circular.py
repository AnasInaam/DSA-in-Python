class Node:
    def __init__(self , data = 0 , next = None):
        self.data = data 
        self.next = next 
class CircularLL:
    def __init__(self):
        self.head = None
    def insertatLast(self):
        if self.head == None:
            self.head = Node(int(input("Enter Your Data: ")))
            self.head.next = self.head
        else:
            temp = self.head 
            while temp.next != self.head:
                temp = temp.next
            temp.next = Node(int(input("Enter Your data:")))
            temp.next.next = self.head
    def insertatFirst(self):
        if self.head == None:
            self.head = Node(int(input("Enter Your Data: ")))
            self.head.next = self.head
        else :
            cur = self.head 
            while cur.next != self.head:
                cur = cur.next 
            temp = Node(int(input("Enter Your Data: ")))
            temp.next = self.head
            self.head = temp
            cur.next = self.head
    def countNode(self):
        if self.head == None:
            print("Circularll is Empty")
        else :
            temp = self.head
            count = 0
            while True:
                count += 1
                temp = temp.next
                if (temp == self.head):
                    break
            return count
    def insertinBetween (self):
        if self.head == None:
            self.head = Node(int(input("Enter Your Data: ")))
            self.head.next = self.head
        else :
            pos = int(input("Enter The Position: "))
            count = self.countNode()
            if pos >= 1 and pos <= count+1:
                if pos == 1:
                    c.insertatFirst()
                elif pos == count+1:
                    c.insertatLast()
                else :
                    pos -= 2
                    temp = self.head
                    while pos > 0:
                        temp = temp.next
                        pos -= 1
                    new = Node(int(input("Enter Your Data: ")))
                    new.next = temp.next 
                    temp.next = new
    def deleteatFirst(self):
        if self.head.next == self.head:
            self.head = None
        else :
            temp = self.head 
            while temp.next != self.head:
                temp = temp.next
            cur = self.head.next
            self.head = cur
            temp.next = self.head

    def deleteatLast(self):
        if self.head == None:
            print("CirclurLL is empty")
        elif self.head.next == self.head:
            self.deleteatFirst()
        else :
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next 
            temp.next.next = None
            temp.next = self.head
    def deleteinBitween(self):
        pos = int(input("Enter The Position of Node: "))
        count = self.countNode()
        if pos >= 0 and pos <= count:
            if pos == 1:
                self.deleteatFirst()
            elif pos == count:
                self.deleteatLast()
            else :
                temp = self.head 
                pos -= 2
                while pos > 0:
                    temp = temp.next
                    pos -= 1
                cur = temp.next.next
                temp.next = cur 
                # cur.next = None
        else :
            print("Invalid Position")
            
    def display(self):
        if self.head == None:
            print("Circularll is Empty")
        else :
            temp = self.head
            while True:
                print(temp.data , end='-->')
                temp = temp.next
                if (temp == self.head):
                    break



c = CircularLL()   
while(1):
    print("\n Menu ")
    print("1. Enter Node at Last")
    print("2. Enter Node at First")
    print("3. Enter Node at Position")
    print("4. Delete Node at first")
    print("5. Delete Node at last")
    print("6. Delete Node at Position")
    print("9. Enter For display ")
    print("10. Enter For Exit")
    choice = int(input("Enter Your Choice: "))
    match(choice):
        case 1:
            c.insertatLast()
        case 2:
            c.insertatFirst()
        case 3:
            c.insertinBetween()
        case 4:
            c.deleteatFirst()
        case 5:
            c.deleteatLast()
        case 6:
            c.deleteinBitween()
        case 9:
            c.display()
        case 10:
            exit()


        
