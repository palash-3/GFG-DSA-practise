#Binary Search using IF

arr = [1,2,3,4,5,6,7]
key = 7

def binary_search(arr, key, low, high):
    if high >= low:
        mid = low+(high-low)//2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, key, low, mid-1)
        else:
            return binary_search(arr, key, mid+1, high)
    else:
        return -1
    
index = binary_search(arr, key, 0, len(arr)-1)
print(index)