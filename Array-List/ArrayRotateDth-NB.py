arr = [1,2,3,4,5,6,7,8,2,145,16,45,84]
d = 8

def ArrayRotation(arr,d):
    for _ in range(d):
        temp = arr[0]
        for j in range(len(arr)-1):
            arr[j] = arr[j+1]

        arr[-1]=temp
    return arr

print(ArrayRotation(arr,d))

