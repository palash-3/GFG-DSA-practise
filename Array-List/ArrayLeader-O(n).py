arr = [16, 17, 4, 3, 5, 2]

def array_leader(arr):
    result = []
    n = len(arr)

    maxRight = arr[-1]
    result.append(maxRight)

    for i in range(n - 2, -1, -1):
        if arr[i] >= maxRight:
            maxRight = arr[i]
            result.append(maxRight)
    result.reverse()
    return result

leader = array_leader(arr)
print(leader)