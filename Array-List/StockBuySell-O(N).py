#arr = [1, 3, 6, 9, 11]
arr = [7, 6, 4, 3, 1]

def buy_and_sell(arr):
    n = len(arr)
    min_value = arr[0]
    max_profit = 0

    for i in range(n):
        min_value = min(min_value, arr[i])
        max_profit = max(max_profit, arr[i]-min_value)
    
    return max_profit

profit = buy_and_sell(arr)
print(profit)
