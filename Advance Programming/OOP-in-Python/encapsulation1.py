class simple:
    def __init__(self):
        self.__balance = 60 
    def setter(self , amount):
        self.__balance = amount
    def getter(self):
        print("Total Amount" , self.__balance)

s = simple()
s.setter(200) 
s.getter()  