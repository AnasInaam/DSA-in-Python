

# class Node:
#     def __init__(self , data = 0 , next = None):
#         self.data = data
#         self.next = next 
# head = Node(5)
# head.next = Node(10)

# print(head.data)


######################### Link list display by while ################################
# class Node:
#     def __init__(self , data = 0 , next = None):
#         self.data = data
#         self.next = next
   
# head = Node(5)
# head.next = Node(10)
# head.next.next = Node(15)

# # print(head.data , head.next.data )

# while head != None:
#     print(head.data , end=' ')
#     head = head.next



# class Node:
#     def __init__(self , data =0 , next = None):
#         self.data = data
#         self.next = next

# class Singlyll:
#     def __init__(self):
#        self.head = None
#     def inserAtLast(self):
#         if self.head == None:
#             self.head = Node(int(input("Enter Data")))
#         else:
#             temp = self.head
#             while temp.next != None:
#                 temp = temp.next
#             temp.next = Node(int(input("Enter Data")))
    
# l = Singlyll()
# l.inserAtLast()
# l.inserAtLast()




class Node:
    def __init__(self, data = 0, next = None):
        self.data = data 
        self.next = next
class singlyll:
    def __init__(self):
       self.head = None

    def insertAtLast(self):
        if self.head == None:
            self.head = Node(int(input("Enter Data: ")))
        else :
            temp = self.head 
            while temp.next:
                temp = temp.next
            temp.next = Node(int(input("Enter Data: ")))
    def display(self):
        temp = self.head 
        while temp != None:
            print(temp.data , end='--> ' )
            temp = temp.next
    def insertatFirst(self):
        if self.head == None:
            self.head = Node(int(input("Enter Data: ")))
        else :
            temp = self.head
            self.head = Node(int(input("Enter Data: ")))
            self.head.next = temp
    def deleteatFirst(self):
        if self.head == None:
            print("Linklist is Empty")
        else:
            temp = self.head.next
            self.head = temp
    def deleteAtLast(self):
        if self.head == None:
            print("Linklist is Empty")
        else:
            temp = self.head
            while (temp.next.next):
                temp = temp.next
            temp.next = None
    def count(self):
        count = 0
        temp = self.head 
        while temp:
            count+=1
            temp = temp.next 
        return count
    def printlist(self):
        list = []
        temp = self.head 
        while temp:
            list.append(temp.data)
            temp = temp.next
        list1 = list[::-1]
        return list1
    def intermediateinsertion(self):
       pos = int(input("Enter The Position: "))
       countofNode = self.count()
       if pos >= 1 and pos <= countofNode+1:
           if pos == 1:
               self.insertatFirst()
           elif pos == countofNode+1:
               self.insertAtLast
           else:
               pos -= 2
               temp = self.head
               while (pos > 0):
                temp = temp.next
                pos -= 1
               new = Node(int(input("Enter Data: ")))
               new.next = temp.next
               temp.next = new
       else:
           print("Invalid Position")
    def specifydelete(self):
        spNode = int(input("Enter Specific Node Postion: "))
        n = int(input("Enter How Many times delete: "))
        temp = self.head
        positionahed = spNode + n -1
        spNode -= 2
        while spNode > 0:
            temp = temp.next
            spNode -=1
        temp2 = self.head
        while positionahed > 0:
            temp2 = temp2.next
            positionahed -=1
        temp.next = temp2
    # display middle in log n
    def middleNode(self):
        middle = int((self.count() /2) )+1
        temp = self.head
        for i in range(middle-1):
            temp = temp.next
        print("this is the middle Node: ", temp.data)



# bubble sort in linklist 
# middle node delete 
    # def Reversell(self):
    #     temp = self.head
    #     count = 0
    #     while temp.next:
    #         count+=1
    #         temp = temp.next
    #         count+=1
    #     # print(temp.data)
    #     last = temp
    #     first = self.head
    #     while (count %2 == 0):
    #         a = last.data
    #         first.data = last
    #         last.data = a
    #         first = first.next 
    #         last = 

            
# Delete specific Node at N time

    
l = singlyll()
while(1):


 print("\nMenu")
 print("1. Insert Node at First")
 print("2. Insert Node at last")
 print("3. Enter Node At Intermediate Postion")
 print("4. Delete Node at First")
 print("5. Delete Node at Last")
 print("6. Delete Specific Node for N times")
 print("7. Display")
 print("8. Count the Nodes")
 print("9. Exit")
 print("10. Reverse Print")
 print("11. Reverse Link List")
 print("12. For Middle Node")
 choice = int(input("Enter your Choice: "))
 match(choice):
    case 1:
        l.insertatFirst()
    case 2:
        l.insertAtLast()
    case 3:
         l.intermediateinsertion()
    case 4:
         l.deleteatFirst()
    case 5:
         l.deleteAtLast()
    case 6:
         l.specifydelete()
    case 7:
        l.display()
    case 8:
         print("Total Count of Node is: ",l.count())
    case 9:
         exit()
    case 10:
        print( l.printlist())
    case 11:
         l.Reversell()
    case 12:
         l.middleNode()
    case _:
        print("Invalid Input")
    

        
 


# l.insertAtLast()
# l.insertAtLast()
# l.insertAtLast()
# l.insertAtLast()
# l.insertatFirst()
# l.deleteatFirst()
# l.display()



