arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]

def remove_duplicate(arr):
    temp_arr = []

    for i in arr:
        if i not in temp_arr:
            temp_arr.append(i)
    return temp_arr

unique_array = remove_duplicate(arr)
print(unique_array)