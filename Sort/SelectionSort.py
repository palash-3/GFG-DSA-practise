arr = [5, 6, 1, 3]

def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

sorted_arr = selection_sort(arr)
print(sorted_arr)