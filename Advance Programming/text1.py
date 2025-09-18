# s1 = {3,4,2,1}
# # s1.remove(3)
# # print(s1)

# # s1.discard(30)
# # print(s1)

# s2 = {3,4,5, 6}
# print(s1.union(s2))
# print(s1&s2)
# print(s1|s2)
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))



# def fun(pack):
#     if pack < 500000:
#         print("No Deduction" , pack)
#     elif pack >= 500000 and pack < 1000000:
#         print("Your Salary inhand" , pack*0.95)
#     elif pack >= 1000000 and pack < 1500000:
#         print("Your Salary inhand" , pack*0.9)
#     elif pack >= 1500000 and pack < 2000000:
#         print("Your Salary inhand" , pack*0.85)
#     else :
#         print("Your Salary inhand" ,pack*0.80 )

# pack = int(input("Enter Package: "))
# fun(pack)

# def fun(pack):
#     if pack < 100:
#         return 0
#     elif pack > 100 and pack < 200:
#         return (pack - 100)*5
#     elif pack > 200 and pack < 300:
#         res = (pack - 100)*5
#         pack -= 100
#         res += (pack - 100)*7
#         return res
#     else :
#         res = (pack - 100)*5
#         pack -= 100
#         res += (pack - 100)*7
#         pack -= 100
#         res += (pack - 100)*10
#         return res
# pack = int(input("Enter unit: "))
# pack = fun(pack)
# print("Your chargers: " , pack)

# 100 zero 
# 100 - 200 -> per unit 5
# 200 - 300 -> per unit 7 
# 300 -> 10

# def fun(pack):
#     if pack <= 100:  
#         return 0
#     elif pack <= 200:  
#         res = (pack - 100) * 5
#         return res
#     elif pack <= 300:  
#         res = 500 + (pack - 200) * 7
#         return res
#     else:   
#         res = 1200 + (pack - 300) * 10
#         return res
# units = int(input("Enter unit: "))
# charges = fun(units)
# print("Your charges:", charges)


# while True:
#     a = int(input("Enter Positivr number: "))
#     if a < 1:
#         continue
#     else :
#         print("thank you")
#         break

# def dis(chai , coffee , pizaa):
#     print("Welcome to the dolly ki Tapri")
#     print("-----------------------------")
#     print("iteams  count  amount ")
#     print("----------------------------")
#     print(f"chai     {chai}      {chai *10} ") 
#     print(f"coffee   {coffee}      {coffee *10} ") 
#     print(f"pizza    {pizza}      {pizza *10} ")
#     print("----------------------------")
#     print(f"Total    {chai+pizza+coffee}      {chai*10+pizza*100+coffee*15}")
#     print("----------------------------")

# chai = coffee = pizza = 0
# while True:
#     print("...........MENU..............")
#     print("For Ordering Chai select 1 , Price = 10RS")
#     print("For Ordering Coffee select 2 Price = 15RS")
#     print("For Ordering Pizza select 3 , Price = 100RS\n")
#     choice = int(input("Enter Your Choice: "))
#     match(choice):
#         case 1:
#             chai +=1
#         case 2:
#             coffee +=1
#         case 3:
#             pizza +=1
#         case 4:
#             dis(chai , coffee , pizza)
#             print("Firse Aayio")
#             exit()
#         case _:
#             print("Please Enter Valid Choice")

# while True:
#     print("...........MENU..............")
#     print("others 1")
#     print("For San , saturday 2\n")
#     choice = (input("Enter Your Choice: "))
#     match(choice):
#         case 'Monday' | 'Thusday' | 'Wednessday' | 'Thursday' | 'Friday':
#             print("Weekday")
#         case 'Sunday' | 'Saturday':
#             print("Weekend")
#         case 5:
#             exit()
#         case _:
#             print("Please Enter Valid Choice")

# while True:
#     choice = int(input("Enter Your Date: "))
#     choice = choice % 7
#     match(choice):
#         case 1:
#             print('Monday')
#         case 2:
#             print('Thusday')
#         case 3:
#             print('Wednessday')
#         case 4:
#             print('Thursday')
#         case 5:
#             print('Friday')
#         case 6:
#             print('Saturday')
#         case 7:
#             print('Sunday')
#         case _:
#             print("Please Enter Valid Choice")
# list1 = []
# for i in range(10):
#     inte = int(input("Enter num: "))
#     list1.append(inte)

# arr = list(map(int , input("Enter the Number by Spaces: ").split()))
# print(arr)

# a , b = map(int , input("Enter Number: ").split())
# print(a*b)

# arr = [i*i for i in range(1, 10)]
# print(arr)

# string = 'Python is a high level language'
# s = string.split()
# arr = [len(i) for i in s]
# print(arr)

# string = 'Python is a high level language'
# s = string.split()
# arr = [i[0].upper() for i in s]
# print(arr)

# string = 'Python is a high level language'
# s = string.split()
# arr = [i[::-1] for i in s]
# str1 = " ".join(arr)
# print(str1)

# arr = list(map(int , input("Enter The Number: ").split()))
# arr = ["even" if i % 2 == 0 else "Odd"  for i in arr]
# print(arr)

# arr = [0 if i % 2== 0 else 1 for i in range(1,10)]
# print(arr)

# s = "ABCD"
# arr = [ord(i) for i in s]
# print(arr)

# s = "12q34586!@#$9o87ykhugmnfcb!@#$%^&"
# arr = [i for i in s if i.isalpha()]
# arr = "".join(arr)
# print(arr)

# s = "12q34586!@#$9o87ykhugmnfcb!@#$%^&"
# arr = [i for i in s if i.isalnum()]
# arr = "".join(arr)
# print(arr)

# s = " Pthon is a highlevel"
# arr= [i for i in s if i in "aeiou"]
# arr = "".join(arr)
# print(arr)  

# s = " Pthon is a highlevel"
# map1= {ch : s.count(ch) for ch in set(s)}
# print(map1)
 
# s = [ "madam" , 'nayan' , 'nitin' , 'meraj']
# list1 = [i for i in s if i == i[::-1]]
# print(list1)

 
# s = [ "madam" , 'nayan' , 'nitin' , 'meraj' , 'Anas']
# list1 = [i for i in s if i[0] in "aieouAIOUE"]
# print(list1)

s = [ "madam" , 'nayan' , 'nitin' , 'meraj' , 'Anas']
list1 = [i for i in s if len(i) % 2== 0]
print(list1)
