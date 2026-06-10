arr = [-2, 6, -3, -10, 0, 2]

def max_subarray_product(arr):
    n = len(arr)
    curr_min = arr[0]
    curr_max = arr[0]
    max_product = arr[0]

    for i in range(1,n):
        temp = max(arr[i], arr[i]*curr_max, arr[i]*curr_min)
        curr_min = min(arr[i], arr[i]*curr_max, arr[i]*curr_min)
        curr_max = temp
        max_product = max(max_product, curr_max)
        
    return max_product

product = max_subarray_product(arr)
print(product)


