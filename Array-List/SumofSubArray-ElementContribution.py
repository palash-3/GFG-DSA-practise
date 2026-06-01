arr = [1, 4, 5, 3, 2]

def sum_of_subarray(arr):
    n = len(arr)
    result = 0

    for i in range(n):
        result+=arr[i]*(i+1)*(n-i)
    
    return result

sum = sum_of_subarray(arr)
print(sum)