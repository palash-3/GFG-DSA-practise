arr = [12, 35, 1, 10, 34, 1]

def second_largest(arr):
    n = len(arr)
    largest = -1
    second_largest = -1

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    for i in range(n):
        if arr[i] > second_largest and arr[i] < largest:
            second_largest = arr[i]
    return second_largest


number = second_largest(arr)
print(number)