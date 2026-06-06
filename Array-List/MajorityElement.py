#arr = [1, 1, 2, 1, 3, 5, 1]
arr = [7]

def majority_element(arr):
    n = int((len(arr)/2))

    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count+=1
        if count > n:
            return arr[i]
    return -1

element = majority_element(arr)
print(element)



