arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]

def remove_duplicate(arr):
    curr = 0
    temp = []
    temp.append(arr[0])

    for i in range(1, len(arr)-1):
        if arr[i] != arr[curr]:
            temp.append(arr[i])
            curr = i
    
    return temp

unique_numbers = remove_duplicate(arr)
print(unique_numbers)