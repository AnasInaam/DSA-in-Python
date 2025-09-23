# int1 = 912
# def digits(digits , sum= 0):
#     str1 = str(digits)
#     if len(str(digits)) >0:
#         return 0
#     else :
#         sum = +int(str1[-1])
#         str1 = str1[:-1]
#         return digits(int(str1) , sum)

# print(digits(int1))


def sumdigits(num):
    if num ==0 :
        return 0
    return 