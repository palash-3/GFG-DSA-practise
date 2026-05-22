arr = [0, 1, 0, 1, 1, 1, 1]

def MaxConsecutive(arr):
    countZero = 0
    countOne = 0
    n = len(arr)

    for i in range(n):
        if arr[i] == 0:
            countZero+=1
            countOne = 0
        else:
            countOne+=1
            countZero = 0
    
    return max(countZero,countOne)

print(MaxConsecutive(arr))