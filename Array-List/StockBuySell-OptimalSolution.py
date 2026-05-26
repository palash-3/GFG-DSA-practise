arr = [100, 180, 260, 310, 40, 535, 695, 30, 20]
#arr = [4, 2]
#arr = [2, 5, 3, 8]

def stock_buy_sell(arr):
    n = len(arr)
    profit = 0

    for i in range(0,n-1):
        if arr[i] < arr[i+1]:
            profit = profit + (arr[i+1]-arr[i])
    return profit

total_profit = stock_buy_sell(arr)
print(total_profit)