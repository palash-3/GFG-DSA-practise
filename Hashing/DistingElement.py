arr = [1, 2, 3, 1, 4, 2]

def remove_duplicate(arr):
    s = set()

    for i in range(len(arr)):
        if arr[i] not in s:
            s.add(arr[i])
    return s

unique_value = remove_duplicate(arr)
print(unique_value)