arr = [5,4,3,2,1,6]

def ArrReverse(arr):
    n = len(arr)

    for i in range(n//2):
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]

    return arr

print(ArrReverse(arr))