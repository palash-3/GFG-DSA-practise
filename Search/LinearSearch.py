arr = [10,20,30,40,50,60]
number = 40

def linear_search(arr, number):
    for i in range(len(arr)):
        if arr[i] == number:
            return i
    return -1

idx = linear_search(arr, number)
print(idx)