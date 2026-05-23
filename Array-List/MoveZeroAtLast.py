arr = [1,2,3,0,4,0,5,0,6]

def MoveZero(arr):
    n = len(arr)
    temp = [0]*n
    count = 0

    for i in range(n):
        if arr[i] != 0:
            temp[i] = arr[i]
            count+=1

    while count < n:
        temp[count] = 0
        count+=1
    
    arr = temp
    print(arr)

MoveZero(arr)