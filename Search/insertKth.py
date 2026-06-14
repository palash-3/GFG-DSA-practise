def searchInsertK(arr, k):  
    left, right = 0, len(arr) - 1  
    while left <= right:  
        mid = left + (right - left) // 2  
        
        # if k is found at mid
        if arr[mid] == k:  
            return mid  

        # if k is smaller, search in left half
        elif arr[mid] > k:  
            right = mid - 1  

        # if k is larger, search in right half
        else:  
            left = mid + 1  

    # if k is not found, return insert position
    return left  

if __name__ == "__main__":  

    arr = [1, 3, 5, 6]  
    k = 5  
    print(searchInsertK(arr, k))