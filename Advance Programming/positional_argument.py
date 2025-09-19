# # positional argument passing 

# def show(a , b):
#     print("name" , a)
#     print("age " , b)

# show("Anas" , 23)

# # Defult argument 
# def show(age = 23):
#     print(age)
# show()


# # keyword based agrument passing 
# from os import name 
# def show(name , age):
#     print("name" , name)
#     print("age " , age)
# show(age = 13 , name = "Anas")


# # Arbitary value passing
# def show(*num): # if i want to pass multiple value 
#     print(num)
#     print(type(num))

# show(1,2,3,4,4,88,66,8,9,8)

# # if i want to pass multiple value in list then how to pass :
# show(*[1,2,3,4,4,88,66,8,9,8])


      
# # Arbiatry keyword based value passing 
# def show(**nums):
#     print(nums)
#     for k , v in nums.items():
#         print(k, ":",v)
# show(name = " Anas" , age = 23 , per = 81.3)

# remove last value
# def show(**nums):
#     print(nums)
#     nums.pop("name")
#     for k , v in nums.items():
#         print(k, ":",v)
    
# show(name = " Anas" , age = 23 , per = 81.3)

