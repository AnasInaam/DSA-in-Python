# file= open("Anas.txt" , "w")
# file.write("Hello, Anas! This is me")

# file = open("Anas.txt" , "r")
# print(file.read())
# file.close()

# file = open("Anas.txt" , "a")
# file.write("\n Anas \n Dhule \n Svkm \n Where is Altamash")
# file.close()

# file = open("Anas.txt" , "w+")
# file.write("deep down you are same as you are as earlier \n but it's not you are underneath \n but what you do \n what defines you \n  ")
# file.seek(0)
# print(file.read())
# file.close()

# file = open("Anas.txt" , "w+")
# file.write("\n \n you die as a hero or live long enough to see yourself become villian")
# file.seek(5, 0)
# print(file.read())

from os import *
# rename("c:/Users/anasm/Desktop/DSA IN PYTHON/Anas_renamed.txt", "c:/Users/anasm/Desktop/DSA IN PYTHON/VS CODE/Anas.txt")

print(getcwd())
print(listdir())

