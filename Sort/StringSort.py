arr = ["GeeksforGeeks", "I", "from", "am"]

def string_sort(arr):
    arr.sort(key=len)
    return arr

sorted_array_string = string_sort(arr)
print(sorted_array_string)
