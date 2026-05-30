arr = [4, 3, 6, 2, 1, 1]

def missing_and_repeating(arr):
    n = len(arr)

    for i in range(n):
        val = abs(arr[i])

        if arr[val-1] > 0:
            arr[val-1] = -arr[val-1]
        else:
            repeating = val
    
    for i in range(n):
        if arr[i] > 0:
            missigng = i+1
            break
    print(repeating, missigng)

missing_and_repeating(arr)

