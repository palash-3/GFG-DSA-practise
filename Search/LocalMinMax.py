arr = [6, 4, 2, -2, 5, 3, 2, 2, -1, -1, 4]

def local_min_max(arr):
    
    
    n = len(arr)
    temp =[]
    temp.append(arr[0])

    for i in range(1, n-1):
        if arr[i] > temp[-1] and arr[i] > arr[i+1]:
            temp.append(arr[i])
        elif temp[-1] > arr[i] and arr[i] < arr[i + 1]:
            temp.append(arr[i])
    
    if temp[-1] != arr[-1]:
        temp.append(arr[-1])

    return temp

result = local_min_max(arr)
print(result)