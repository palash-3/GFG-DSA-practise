arr = [1, 2, 3, 4, 5]

def ArrayWave(arr):
    n = len(arr)

    for i in range(0,n-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

    print(arr)

ArrayWave(arr)