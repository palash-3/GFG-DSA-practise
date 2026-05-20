arr = [1,2,3,4,5,6,7,8,145,16,45,84]
d = 8

def ArrayRotation(arr,d):
    temp = []
    temp = arr[d:] + arr[0:d]
    arr = temp
    return arr

print(ArrayRotation(arr,d))
