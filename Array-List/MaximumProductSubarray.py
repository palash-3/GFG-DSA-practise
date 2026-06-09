#arr = [-2, 6, -3, -10, 0, 2]
#arr = [-1, -3, -10, 0, 6]
arr = [2, 3, 4] 

def max_aubarray_product(arr):
    n = len(arr)
    max_product = arr[0]

    for i in range(n-1):
        curr_product = 1
        for j in range(i,n):
            curr_product = curr_product*arr[j]
            max_product = max(max_product, curr_product)
    return max_product

product = max_aubarray_product(arr)
print(product)