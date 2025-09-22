coins = [1 ,5 ,2 , 10 , 25]
coins.sort(reverse = True)
t = 65 
g = 0
arr = []
map1 = {}
for coin in coins:
    while coin <= t:
        t -= coin 
        arr.append(coin)
        g +=1
print(g)
print(arr)


