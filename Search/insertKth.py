arr = [1, 3, 5, 6]
k = 2

def insert_k(arr, k):
    n = len(arr)
    
    for i in range(n):
        if k <= arr[i]:
            return i
    return -1

idx = insert_k(arr, k)
print(idx)
