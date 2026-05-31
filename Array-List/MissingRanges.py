arr = [14, 15, 20, 30, 31, 45]
lower = 10
upper = 50

def missing_range(arr, lower, upper):
    n= len(arr)

    if lower != arr[0]-1:
        print([lower, arr[0]-1])

    for i in range(n-1):
        if arr[i]+1 != arr[i+1]:
            print([arr[i]+1, arr[i+1]-1])
    
    if upper > arr[-1]:
        print([arr[-1] + 1, upper])


missing_range(arr, lower, upper)