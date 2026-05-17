arr = [5,4,3,2,1,6]

def ArrReverse(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left = left+1
        right = right-1
    
    return arr

print(ArrReverse(arr))