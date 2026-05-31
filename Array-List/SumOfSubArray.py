arr = [1, 4, 5, 3, 2]

def subarray_sum(arr):
    n = len(arr)
    total_sum = 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum = current_sum+arr[j]
            total_sum = total_sum+current_sum
    return total_sum

sum = subarray_sum(arr)
print(sum)