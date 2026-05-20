arr = [1,2,3,4,5]

def arrayRev(arr):
    n = len(arr)
    reverse_array = []
    #reverse_array = [0]*n

    for i in range(n-1,-1,-1):
        #reverse_array[n-1-i] = arr[i]
        reverse_array.append(arr[i])
    
    print(reverse_array)

arrayRev(arr)