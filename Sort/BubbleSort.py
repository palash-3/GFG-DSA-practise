arr = [5, 6, 1, 3]

def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        swapped = False

        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

sorted_arr = bubble_sort(arr)
print(sorted_arr)