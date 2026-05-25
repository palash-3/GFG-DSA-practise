arr = [1, 3, 6, 9, 11]
#[7, 6, 4, 3, 1]

def stock_buy_sell(arr):
    n = len(arr)
    max_difference = 0

    for i in range(n):
        for j in range(i, n):
            current_difference = arr[j] - arr[i]
            max_difference = max(max_difference, current_difference)
    
    return max_difference

profit = stock_buy_sell(arr)
print(profit)
