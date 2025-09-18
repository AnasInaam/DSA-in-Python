class Node:
    def __init__(self , data =0 , next = None , prev = None):
        self.data = data
        self.next = next
        self.prev = prev
class dublyll:
    def __init__(self):
        self.head = None
    def insertatLast(self):
        if self.head == None:
            self.head = Node(int(input("Enter Data: ")))
        else :
            temp = self.head
            while temp.next != None:
                temp = temp.next 
            new = Node(int(input("Enter Data: ")))
            temp.next = new
            temp.next.prev = temp

    def insertatFirst(self):
        if self.head == None:
            self.head = Node(int(input("Enter Data: ")))
        else :
            temp = Node(int(input("Enter Data: ")))
            temp.next = self.head
            self.head = temp
            self.head.next.prev = self.head
    def display(self):
        if self.head == None:
            print("Doubly List is Empty")
        temp = self.head 
        while temp != None:
            print(temp.data , end='--> ' )
            temp = temp.next 
    def diplaybyPrev(self):
        temp = self.head 
        while temp.next != None:
            temp = temp.next 
        cur = temp
        while cur != None:
            print(cur.data , end='--> ' )
            cur = cur.prev
    def deleteatFirst(self):
        if self.head == None:
            print("Dublyll Is empty")
        else :
            temp = self.head 
            self.head = temp.next
            self.head.prev = None
    def deleteatLast(self):
        if self.head == None:
            print("Dublyll Is empty")
        else :
            temp = self.head 
            while temp.next.next != None:
                temp = temp.next
            temp.next = None 
            temp.prev = None


d = dublyll()
   
while(1):
    print("\n Menu ")
    print("1. Enter Node at Last")
    print("2. Enter Node at First")
    # print("3. Enter Node at Position")
    print("4. Delete Node at first")
    print("5. Delete Node at last")
    # print("6. Delete Node at Position")
    print("9. Enter For display ")
    print("10. Enter For Exit")
    print("11. Display in Reverse")
    choice = int(input("Enter Your Choice: "))
    match(choice):
        case 1:
            d.insertatLast()
        case 2:
            d.insertatFirst()
        # case 3:
        #     c.insertinBetween()
        # case 4:
            d.deleteatFirst()
        case 5:
            d.deleteatLast()
        # case 6:
        #     c.deleteinBitween()
        case 9:
            d.display()
        case 10:
            exit()
        case 11:
            d.diplaybyPrev()
        case _:
            print("Invalid Choice")


        
