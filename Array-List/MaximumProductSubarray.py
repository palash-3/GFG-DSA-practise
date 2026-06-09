arr =[-2, 6, -3, -10, 0, 2]

def max_product(arr):
    n = len(arr)
    maxProd = arr[0]

    for i in range(n):
        mul = 1
        for j in range(i, n):
            mul *= arr[j]
            maxProd = max(maxProd, mul)
    
    return maxProd

product = max_product(arr)
print(product)