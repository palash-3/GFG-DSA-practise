arr = [0, 1, 0, 0, 0, 1, 1, 1, 1]

def MaxConsecutive(arr):
    n = len(arr)
    maxCount = 0
    count = 1

    for i in range(1, n):
        if arr[i] == arr[i-1]:
            count+=1
        else:
            maxCount = max(maxCount,count)
            count = 1
    return max(maxCount, count)

print(MaxConsecutive(arr))