class Student:
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.m1 = int(input("Enter marks for subject 1: "))
        self.m2 = int(input("Enter marks for subject 2: "))
        self.m3 = int(input("Enter marks for subject 3: "))
    def calculate_per(self):
        self.total = self.m1 + self.m2 + self.m3
        self.per = (self.total / 300)* 100
        
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:")
        print("Subject 1:", self.m1)
        print("Subject 2:", self.m2)
        print("Subject 3:", self.m3)
        print("Total Marks:", self.total)
        # why self.total 
        print("Percentage:", self.per)

s1 = Student()
s1.calculate_per()
s1.display()