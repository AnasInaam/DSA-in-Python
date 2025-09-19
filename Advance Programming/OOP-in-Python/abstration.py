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


from abc import ABC, abstractmethod

class arithmeticOp(ABC):   # abstract bas class which contain min one abdstract class
    @abstractmethod   # this is decorater 
    def __init__(self , a ,b):
        pass
class Add(arithmeticOp):
    def __init__(self ,a ,b):
        print("This is the Addition" , a+b)

class sub(arithmeticOp):
    def __init__(self ,a , b):
        print("this is the substration" , abs(a-b))

# usage
a = Add(10 , 20)
b = sub(10 , 20 )