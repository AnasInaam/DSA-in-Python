# def fact1(n):
#     if n == 0:
#         return 1
#     fact = 1
#     fact = fact*n
#     return fact1(n-1)
# print(fact1(5))

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
# print(fact(5))

# def pow(a , b):
#     if b == 1:
#         return a
#     return a * pow(a , b-1)
# print(pow(2 ,5))

# def pow(a ,b):
#     if b == 1:
#         return a
#     return a * pow(a , b-1)


# def digit(n):
#     if n == 0:
#         return 0
#     return 1+digit(n // 10)
# print(digit(1234567890))

# def sum(n):
#     if n == 0:
#         return 1
#     return  n % 10 * sum(n // 10)
# print(sum(25))

# def reverse(n, rev=0):
#     if n == 0:
#         return rev
#     return reverse(n // 10, rev * 10 + n % 10)

# print(reverse(1234))  


# def string(s , rev = ""):
#     if len(s) == 0:
#         return rev
#     rev += s[-1]
#     return string(s[:-1], rev)
# print(string("Hello"))



# def fib(n):
#     list1  = [ 0 , 1]
#     for i in range(2 , n):
#         list1.append(list1[i-1] + list1[i-2])
#     return list1

# list2 = fib(8)
# print(list2)

# by Recursion fib
# def fib(n):
#    a = 0 
#    b = 1
#    if n == 0:
#        return a
#    elif n == 1:
#        return b
#    else:
#        return fib(n-1) + fib(n-2)
# print(fib(7))
    
# recusion by binary 
def binary(ar , key , low , high):
    if low > high :
         return -1 
    mid = (low+high) //2
    if (ar[mid] == key):
         return mid
    elif ar[mid] < key:
         return binary(ar , key , mid+1 , high)
    else :
         return binary(ar , key  , low , mid -1)

ar = [1,2,3,4,5,6,7,8,9]
key = 7
low = 0
high = len(ar) - 1
print(binary(ar , key , low , high))
# ctxt.io/2/AAD46J9XEA


# def binarysearch( self,arr,k):
#             low = 0
#             high = len(arr) - 1
#             while low <= high:
                
#                 mid = (low + high) // 2
        
#                 if arr[mid] == k:
#                     return mid
        
#                 elif arr[mid] < k:
#                     low = mid + 1
        
#                 elif arr[mid] > k:
#                     high = mid - 1
        
#             return -1



# return 40 + 123
# return 30 + 12
# return 20 + 1
# return 10 + 0

# return 40 + 123
# return 30 + 12
# return 20 + 1
# return 10 + 0






