#abstraction program 

# from abc import ABC, abstractmethod

# class arithmeticOp(ABC):   # abstract bas class which contain min one abdstract class
#     @abstractmethod   # this is decorater 
#     def calc(self):
#         pass
# class Add(arithmeticOp):
#     def calc(self):
#         a , b = 10 , 20
#         print("This is the Addition" , a+b)

# class sub(arithmeticOp):
#     def calc(self):
#         a , b = 10 , 20
#         print("this is the substration" , abs(a-b))

# # usage
# a = Add()
# a.calc()
# b = sub()
# b.calc()

# tranfer statement :
# break , continue , pass 
# break : it is used to terminate the loop or switch statement
# continue : it is used to skip the current iteration of the loop and move to the next iteration
# pass : it is used to indicate that a block of code is intentionally left empty    


# from abc import ABC, abstractmethod

# class arithmeticOp(ABC):   # abstract bas class which contain min one abdstract class
#     @abstractmethod   # this is decorater 
#     def __init__(self , a ,b):
#         pass
# class Add(arithmeticOp):
#     def __init__(self ,a ,b):
#         print("This is the Addition" , a+b)

# class sub(arithmeticOp):
#     def __init__(self ,a , b):
#         print("this is the substration" , abs(a-b))

# # usage
# a = Add(10 , 20)
# b = sub(10 , 20 )


# from abc import ABC, abstractmethod

# class arithmeticOp(ABC):   # abstract bas class which contain min one abdstract class
#     @abstractmethod   # this is decorater 
#     def calc(self):
#         pass
# class Add(arithmeticOp):
#     def __init__(self ,a ,b):
#         self.a = a 
#         self.b = b
#     def calc(self):
#         print("This is the Addition" , a+b)

# class sub(arithmeticOp):
#     def __init__(self ,a ,b):
#         self.a = a 
#         self.b = b
#     def calc(self ):
#         print("this is the substration" , abs(a-b))

# # usage
# a = Add(10 , 20)
# a.calc()
# b = sub(10 , 20 )
# b.calc()

# from abc import ABC, abstractmethod

# class arithmeticOp(ABC):   # abstract bas class which contain min one abdstract class
#     @abstractmethod   # this is decorater 
#     def calc(self):
#         pass
# class Add(arithmeticOp):
#     def __init__(self ,a ,b):
#         self.a = a 
#         self.b = b
#     def calc(self):
#         print("This is the Addition" , a+b)
# class res:
#     def result(self , a , b):
#         print(f"this is the {a} and {b} values")
        
# class sub(arithmeticOp , res):
#     def __init__(self ,a ,b):
#         self.a = a 
#         self.b = b
#     def calc(self ):
#         print("this is the substration" , abs(a-b))
#         self.result(a , b)


# # usage
# a = Add(10 , 20)
# a.calc()
# b = sub(10 , 20 )
# b.calc()




# class arithmeticOp:   # abstract bas class which contain min one abdstract class
#     def calc(self):
#         pass
# class Add:
#     def __init__(self ,a ,b):
#         self.a = a 
#         self.b = b
#     def calc(self):
#         print("This is the Addition" , self.a+self.b)
# class res:
#     def result(self , a , b):
#         print(f"this is the {a} and {b} values")
        
# class sub(res):
#     def __init__(self ,a ,b):
#         self.a = a 
#         self.b = b
#     def calc(self ):
#         print("this is the substration" , abs(self.a-self.b))
#         self.result(self.a , self.b)

# # usage
# a = Add(10 , 20)
# a.calc()
# b = sub(10 , 20 )
# b.calc()



class Add:
    def add(self, a, b):
        print("Addition of numbers is:", a + b)

class Sub:
    def sub(self, a, b):
        print("Subtraction of numbers is:", a - b)

class UserInput:
    def get_input(self):
        a = int(input("Enter Num: "))
        b = int(input("Enter Num: "))
        return a, b

class Calc(Sub, Add, UserInput):
    def calc(self):
        while True:
            print("\nMenu")
            print("For Addition press : 1")
            print("For Subtraction press : 2")
            print("For Exit press : 3")
            choice = int(input("Enter the Choice: "))
            match choice:
                case 1:
                    a, b = self.get_input()
                    self.add(a, b)
                case 2:
                    a, b = self.get_input()
                    self.sub(a, b)
                case 3:
                    print("Exiting...")
                    exit()
                case _:
                    print("Invalid Choice")

# run
c = Calc()
c.calc()
