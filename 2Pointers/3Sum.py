arr = [1, 4, 45, 6, 10, 8]
target = 13

def hasTripletSum(arr, target):
    n = len(arr)
    arr.sort()
    
    # Fix the first element as arr[i]
    for i in range(n - 2):
        l = i + 1
        r = n - 1
        
        requiredSum = target - arr[i]
        while l < r:
            if arr[l] + arr[r] == requiredSum:
                return True
            if arr[l] + arr[r] < requiredSum:
                l += 1
            else:
                r -= 1
    
    return False

print(hasTripletSum(arr, target))