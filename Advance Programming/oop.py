# class cla:
#     def __init__(self ,a ,b):
#         res = self.add(a, b)  
#         self.num = res
#         print("Constructor called, sum is:", self.num)

#     def add(self, a, b):
#         return a + b

# c = cla(10, 20)
  
class Simple:
    def __init__(self):
        self.a = int(input("Enter Value a: "))
        self.b = int(input("Enter Value b: "))

class Simple2(Simple):          
    def __init__(self):
        super().__init__()      
        res = self.a + self.b
        print("Sum:", res)

s2 = Simple2()

# print(s2.sum(10, 20)) 

#in multiple inheritance which function is run 
#   A   B
#     C

# class A:
#     show()

# class B(A):
#     show()

# class C(B):
#     show()
#     super().__init__
#     then class B function call 

# c.show()



