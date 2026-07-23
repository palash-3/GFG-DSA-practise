arr = [0,1,0,3,12]

def move_zeros(arr):
    n = len(arr)
    zero_track = 0

    for i in range(n):
        if arr[i] != 0:
            if arr[i] != 0:
                arr[zero_track], arr[i] = arr[i], arr[zero_track]
            zero_track+=1
    return arr


        


result = move_zeros(arr)
print(result)