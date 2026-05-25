arr = [100, 180, 260, 310, 40, 535, 695, 30, 20]
#arr = [4, 2]
#arr = [2, 5, 3, 8]

def stock_buy_sell(arr):
    local_minima = arr[0]
    local_maxima = arr[0]
    total_profit = 0
    n = len(arr)
    i = 0

    while i < n-1:
        while i < n-1 and arr[i] >= arr[i+1]:
            i+=1
        local_minima = arr[i]

        while i < n-1 and arr[i] <= arr[i+1]:
            i+=1
        local_maxima = arr[i]

        total_profit = total_profit + (local_maxima-local_minima)

    return total_profit
    
profit = stock_buy_sell(arr)
print(profit)