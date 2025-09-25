b = 5 
a = 0 
b = 1
n = int(input("Enter the number : "))

# def fib(a , b , n):
#     if n == 0:
#         return 
#     print(a)
#     fib(a+b , a , n-1)

def fib(n):
    if n <=1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(n))