def kanpsack(profits , weights , capacity):
    items = []
    for i in range(len(profits)):
        ratio = profits[i] / weights[i]
        items.append((profits[i] , weights[i] , ratio))
    items.sort(key = lambda x : x[2] , reverse=True)
    total_profit = 0.0
    remaining_capacity = capacity
    for profit , weight , ratio in items:
        if remaining_capacity == 0:
            break
        if weight <= remaining_capacity :
            total_profit += profit
            remaining_capacity -= weight
        else :
            total_profit += ratio * remaining_capacity
            remaining_capacity = 0
    return total_profit
profits = [60 , 100 , 120]
weights = [10 , 20 , 30 ]
capacity = 50
print(kanpsack(profits , weights , capacity))