arr = [1, 2, 3, 4, 6, 7, 8]

def missingNumber(arr):
    n = len(arr)+1
    for i in range(n-1):
        if arr[i] != i + 1:
            return i + 1         
    return n
number = missingNumber(arr)
print(number)