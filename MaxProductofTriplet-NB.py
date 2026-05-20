#arr = [10, 3, 5, 6, 20]
arr = [-10, -3, -5, -6, -20]

def MaxProduct(arr):
    maxProduct = -10**9
    n = len(arr)

    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                product = arr[i]*arr[j]*arr[k]
                maxProduct = max(maxProduct, product)
    return maxProduct

print(MaxProduct(arr))