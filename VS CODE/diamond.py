# x = int (input("Enter The Number Of Rows For The Diamond Pattern: "))
# diamond = '*'
# # for i in range(0 , x+1):
# #     print(diamond *i)
# # for j in range(x , 0 , -1):
# #     print(diamond *j)
# # Diamond pattern
# n = x  # height of diamond

# Upper part
# for i in range(1, n+1):
#     print(" " * (n-i) + "*" * (2*i-1))

# # Lower part
# for i in range(n-1, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# for i in range(1 , n+1):
#     print(" " * (n -i) + "*" *(2*i-1))
# fact =1
# for i in range(n):
#     fact = n * fact 
#     n -=1
# print(fact)
check = int(input("Enter The Number To Check Prime Or Not: "))

def is_prime(y):
    if y <= 1:
        return False  # directly return
    for i in range(2, int(y**0.5) + 1):
        if y % i == 0:
            return False  # stop immediately if divisible
    return True  # if no divisor found, then prime

# calling the function
if is_prime(check):
    print("True")
else:
    print("False")

# from sympy import isprime
# print(isprime(x))


    


