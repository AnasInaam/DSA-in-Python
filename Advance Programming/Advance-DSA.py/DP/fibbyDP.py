def fib(n , memo):
    if n in memo:
        return memo
    if n <= 1:
        return n
    memo[n] = fib(n-1 , memo) + fib(n-2 , memo)
    return memo[n]

n = 7
print(fib(n))



