arr = [1, 2, 0, 4, 3, 0, 5, 0]

def MoveZero(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count+=1


    while count < n:
        arr[count] = 0
        count+=1
    
    print(arr)

MoveZero(arr)
