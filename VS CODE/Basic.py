 #################### PRINTING AND OUTPUT ####################
# Print to stdout and file
# import sys
# print("Hello, World!", file=sys.stdout)
# with open("output.txt", "w") as f:
#     print("Hello, World!", file=f)


#################### LOOPS AND TIME ####################
# import time
# I = 0
# while I <= 1:
#     time.sleep(1)
#     print("ANAS", flush=False)
#     I += 1


#################### VARIABLES AND CONSTANTS ####################
# a: int = 10  # constant by convention, use uppercase for constants


# x = 10
# del x
# print("x has been deleted")


#################### KEYWORDS ####################
# import keyword
# print("Keywords in Python:", keyword.kwlist)
# print("Number of keywords in Python:", len(keyword.kwlist))




#################### BASIC OPERATIONS ####################
# x = 20
# r = x + 30
# print("The value of x is:", x)
# x = 2e3
# print(x)
# print(type(x))
# c1 = 3+4j
# print(c1, type(c1))


#################### STRING IMMUTABILITY ####################
# Strings are immutable: cannot change characters after creation.
# To "modify" a string, convert to list, change, then join back.


#################### ARRAYS AND LISTS ####################
# Python lists can store any type. For numeric arrays, use array module or numpy.
# arr = [1, 2, 3, 4]
# import array
# arr = array.array('i', [1, 2, 3, 4])
# import numpy as np
# arr = np.array([1, 2, 3, 4])


#################### SETS ####################
# set1 = {2,3,4,4,520,55,3,2,1,0}
# print(set1)
#

#################### DICTIONARY (dict) ####################
# Python dict is like C++ map/unordered_map.
# d = {"apple": 5, "banana": 10}
# print(d["apple"])
#

#################### BITWISE OPERATORS ####################
# a = 5  # 0b0101
# b = 3  # 0b0011
# print(a & b)   # 1
# print(a | b)   # 7
# print(a ^ b)   # 6
# print(~a)      # -6
# print(a << 1)  # 10
# print(a >> 1)  # 2



#################### MEMBERSHIP & IDENTITY OPERATORS ####################
# in / not in: check if value in sequence
# is / is not: check if two variables point to same object
# a = [1, 2, 3]
# b = a
# c = list(a)
# print(a is b)   # True
# print(a is c)   # False


#################### TERNARY OPERATOR ####################
# x = 5
# y = 10
# min_value = x if x < y else y
# print("The minimum value is:", min_value)


#################### MATH FUNCTIONS ####################
# import math
# math.floor(x): largest int <= x
# math.ceil(x): smallest int >= x
# print("Floor of 5.7:", math.floor(5.7))
# print("Ceil of 5.7:", math.ceil(5.7))


#################### ESCAPE SEQUENCES ####################
# \n: New line, \t: Tab, \\: Backslash, \r: Carriage return, \b: Backspace
# print("1\t2")
# print("123456789\rWorld")
# print("123456789\b\b\b\b\bAB")
# print('C:\\Users\\anasm\\Desktop\\DSA BY PYTHON\\VS CODE')
# print(r"\n\b\t\\")  # Raw string


#################### FOR LOOPS ####################
# for i in range(10):
#     print(i)


#################### UNICODE VS ASCII ####################
# ASCII: 7-bit, 128 chars. Unicode: covers all world scripts, >143,000 chars.


#################### INPUT AND SPLIT ####################
# name = input("Enter your name: ")
# print("Hello, " + name + "!")
# x, y = input("Enter two numbers separated by space: ").split()
# print(type(x), type(y))
# x = input("Enter a new value for x: ").split()
# print(type(x))
# x = "Hello Anas, how are you?".split("a")
# print(x)
# roll, name = input("Enter your roll number and name separated by comma: ").split(",")
# print("Roll Number:", roll)
# print("Name:", name)


#################### PYTHON ERROR TYPES ####################
# 1. SyntaxError: Code not written correctly (e.g. missing parenthesis)
# 2. IndentationError: Indentation missing or inconsistent
# 3. NameError: Variable/function not found
# 4. TypeError: Operation on wrong type
# 5. ValueError: Correct type, wrong value
# 6. IndexError: Invalid index in list/tuple
# 7. KeyError: Dict key not found
# 8. AttributeError: Invalid attribute for object
# 9. ImportError/ModuleNotFoundError: Import fails
# 10. ZeroDivisionError: Division by zero


#################### CONTROL STATEMENTS ####################
# if x > 0:
#     print("Positive")
# elif x < 0:
#     print("Negative")
# else:
#     print("Zero")
# for i in range(5):
#     print(i)
# while x < 5:
#     print(x)
#     x += 1



#################### IF-ELIF-ELSE EXAMPLE ####################
# age = 18
# if age >= 18:
#     print("You are eligible to vote.")
# elif age >= 16:
#     print("You can drive with a learner's permit.")
# else:
#     print("You are too young to drive.")


#################### WHILE LOOP WITH ELSE ####################
# i = 1
# while i <= 5:
#     print(i, end='')
#     i += 1
#     break
# else:
#     print("Loop ended")


#################### MATCH CASE (PYTHON 3.10+) ####################
# match case is like switch-case but more powerful (pattern matching)
# choice = int(input("Enter Your choice: "))
# match choice:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case _:
#         print("Invalid input")

# choice = int(input("Enter Your choice: "))
# match choice:
#     case 1|2|3|4:
#         print("One")
#     case 5|6|7|8:
#         print("Two")
#     case _:
#         print("Invalid input")

# # match case using list of tuple :
# i= (11 ,22 ,33)
# match i:
#     case [1|2|3]:
#         print("One")
#     case [11|22|33]:
#         print("Two")
#     case _:
#         print("Invalid input")

# Collecting user input for list
# li = []
# for i in range(5):
#     li.append(int(input("Enter a number: ")))
# print(li)

# li = (input("Enter a number: ")).split()
# for i in range(len(li)):
#     li[i] = int(li[i])
# print(li)

# Homework: Dictionary in match case.

# add
# square
# triangle area
# area of circle

# while(1):
#     choice = int(input("Enter Your choice 1:Addition 2:Square 3:Area of Triangle 4:Area of Circle : "))
#     match choice:
#         case 1:
#             print ("Your choice is addition")
#             a = int(input("Enter first number: "))
#             b = int(input("Enter second number: "))
#             print("The Addition of these Number is: " , a+b)
#         case 2:
#             print("Your choice is Square")
#             x = int(input("Enter the size of square: "))
#             print("The square of this number is: ", x*x)
#         case 3: 
#             print("Your choice is Area of Triangle")
#             base = int(input("Enter the base of triangle: "))
#             height = int(input("Enter the height of triangle: "))
#             print("The area of Triangle is: ", 1/2 * base * height)
#         case 4:
#            print("Your choice is Area of Circle")
#            radius = int(input("Enter the radius of circle: "))
#            print("The area of Circle is: ", 3.14 * radius * radius)
#         case _:
#            print("Please Enter a valid choice")
# how to exit the while(1) loop :
# exit()


# student = {
#     'name': 'John',
#     'age': 21,
#     'city': 'New York'
# }

# print(student)
# print(student['name'])

# student1 = {}

# student1['roll'] = int(input("Enter your roll number: "))
# student1['name'] = input("Enter your name: ")
# print(student1['name'])

# List of dictionaries :
# n  = int(input("Enter the number of students: "))
# students = []
# for i in range(n):
#     student = {}
#     student['roll'] = int(input("Enter your roll number: "))
#     student['name'] = input("Enter your name: ")
#     students.append(student)
# print(students)

# per = int(input("Enter the number of students: "))

# match per:
#     case per if per >=80 and per <= 100:
#         print("Distinction")
#     case per if per >= 60 and per < 80:
#         print("First Class")
#     case per if per >= 40 and per < 60:
#         print("Second Class")
#     case _:
#         print(f"{per} students entered:")

# # More about the string 
# a = 'I am '
# y = 'a student.'
# print(a + y)

# print("Anas", * 4)
# x = 'Mohammad Anas'
# print(x[:]) # Full string
# print(x[4]) # m which is at index 4
# print(x[:3]) # Moh which is at index 0 to 2
# print(x[2:5]) # ham which is at index 2 to 4
# print(x[:-1]) # Mohammad Ana which is at index 0 to -1
# print(x[::2]) # means take every second character
# print(x[::-1])  # Reverse the string

# m = 'meraj'
# print(m[::-1]) # jarem

# # string function

# print(m.upper()) # MERAJ
# print(m.lower()) # meraj
# print(m.title()) # Meraj
# print(m.capitalize()) # Meraj
# print(m.swapcase()) # JERAJ
# print(m.count('a')) # 2
# print(m.find('a')) # 2
# print(m.find('z')) # -1
# print(m.index('a')) # 2
# print(m.index('z')) # ValueError: substring not found
# print(m.replace('a', 'o')) # meroj

# # strip function
# var = "    Altamash  "
# print("***" + var.strip()+ "***" , sep="") # 'Altamash'
# print("**" + var.lstrip()+ '**', sep="") # 'Altamash  '
# print("**" + var.rstrip()+ '**', sep="") # '    Altamash'

# var1 = "hi abc def abc pqr abc a"
# print(var1.find('abc' , 5)) # 11
# print(var1.index('abc' , 5)) # 11
# # find all abc in this index number without predefine function
# start = 0
# for i in range(len(var1)-2):
#     if var1[i] == 'a' and var1[i+1] == 'b' and var1[i+2] == 'c':
#         #    if var1[i:i+3] == 'abc':
#         print("Found 'abc' at index:", i)


# find all abc in this index number without predefine function
# start = 0
# while True:
#     start = var1.find('abc', start)
#     if start == -1:
#         break
#     print("Found 'abc' at index:", start)
#     start += 1

# while "abc" in var1:
#     start = var1.find('abc', start)
#     var1 = var1.replace('abc', 'QQQ', 1)
#     if start == -1:
#         break
#     print("Found 'abc' at index:", start)

# walrus operator information :
# The walrus operator (:=) allows you to assign a value to a variable as part of an expression.
# This can be useful for simplifying code and avoiding repetition.
# For example:
# print(x := 5)

# x = [5 ,10 ,15 ,20 , 25]
# i = 0
# print ( t := [5 ,10 ,15 ,20 , 25])


# while i < (n := len(x)):
#     print(x[i] , end=' ')
#     i += 1

# precision issues :
# When dealing with floating-point numbers, precision issues can arise due to the way they are represented in memory.
# z = 0.1 + 0.2
# print("0.1 + 0.2 =", z)  # Output may not be exactly 0.3 due to precision issues
# # To avoid precision issues, consider using the decimal module for precise decimal arithmetic.
# from decimal import Decimal
# p = Decimal('0.1') + Decimal('0.2')
# print("0.1 + 0.2 =", p)  # Output will be exactly 0.3


# if z == 0.3:
#     print(True)
# else:
#     print(False)


# if float(p) == 0.3:
#     print(True)
# else:
#     print(False)

# import random as r
# print(int(r.random() * 100))  # Random number between 0 and 99
# print(int(r.uniform(1, 10)))  # Random float between 1 and 10
# print(int(r.random() ))


# More on list
# empty list
# empty_list = []
# print(empty_list)
# # mixture datatype list
# mixed_list = [1, "two", 3.0, True]
# print(mixed_list)

# nested_list = [1, 2, [3, 4], 5]
# print(nested_list)
# print(nested_list[2][1])  # Accessing element in nested list

# # Accessing element list slicing
# x = [1, 2, 3, 4, 5 , 2 ,4 ,2]
# print(x[1:4])  # Slicing from index 1 to 3

# y = [6, 7, 8, 9, 10]
# x.extend(y)  # Extending list x with elements of y
# # x = x+y
# print(x)
# x.remove(2)  # Removing element 2 from list x
# print(x)

# while 2 in x:
#     x.remove(2)
# print(x)



 # how to use list comprehension:

# squared_numbers = [x*x for x in range(10)]
# print(squared_numbers)

# x = []
# for i in range(10):
#     x.append(i*i)
# print(x)

# li = [i*i for i in range(1, 7)]
# print(li)

# li1=[int(input("Enter a number: ")) for i in range(5)]
# print(li1)

# x = [1, 2, 3, 4, 5]
# y = [i for i in x if (i % 2 == 0)]
# print(y)


# Z = [ "Hello", "World", "Python", "Programming"]
# Y = [i.upper() for i in Z]
# print(Y)

# si = ["12the 3 th ansme13 e f s24 s q y987 "]
# sii = [i for i in si if i.isdigit()]

# sen = ["do study hard for your placement exams"]
#  # reverse the sen string word by word not letter by letter
# seen = [i.split()[::-1] for i in sen]
# print(seen)

# x = [[1,2] , [3,4], [5,6]]
# y = [j for i in x for j in i]
# print(y)

# print this by list comprehension
# [(1,1) , (2,4) , (3,9) , (4,16) , (5,25) , (6,36)]

# squares = [(i, i*i) for i in range(1, 7)]
# print(squares)

# x = [ 5 , "Kunal" , 23,234.34 ]
# y = [i for i in x if type(i) == int]
# print(y)

# if else in list comprehension

#################### LIST COMPREHENSION AND PRIME CHECK ####################
a = [23, -34 , 45 ,29 , 98,-3]
# b = [0 if i > 0 else i for i in a]
# print(b)
# c = [i for i in a if i > 1 and all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
# print(c)
from sympy import isprime
# Using sympy to check for prime numbers in a list
s = [i for i in a if isprime(i) and (1 ,50)]
# search shortcut in VS Code: ctrl + f

#################### MISCELLANEOUS ####################
# 242 + 242 = 484