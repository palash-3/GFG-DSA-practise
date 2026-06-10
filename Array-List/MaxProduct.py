#Traversing both side

arr = [-2, 6, -3, -10, 0, 2]

def max_subarray_product(arr):
    n = len(arr)
    left_to_right = 1
    right_to_left = 1
    max_product = float('-inf')

    for i in range(n):
        if left_to_right == 0:
            left_to_right = 1
        if right_to_left == 0:
            right_to_left = 1
        
        left_to_right *= arr[i]

        j = n - i - 1
        right_to_left *= arr[j]

        max_product = max(max_product, left_to_right, right_to_left)
    return max_product

product = max_subarray_product(arr)
print(product)