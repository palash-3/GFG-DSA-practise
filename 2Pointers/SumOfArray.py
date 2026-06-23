arr = [-3, -1, 0, 1, 2]
target = -2

def two_sum(arr, target):
    left = 0
    right = len(arr)-1

    while left < right:
        if arr[left] + arr[right] == target:
            return [left, right]
        elif arr[left] + arr[right] < target:
            left+=1
        else:
            right-=1
    return None

idx = two_sum(arr, target)
print(idx)
