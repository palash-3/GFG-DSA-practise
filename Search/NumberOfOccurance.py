# arr = [1, 1, 2, 2, 2, 2, 3]
# target = 2
arr = [1, 1, 2, 2, 2, 2, 3]
target = 5

def number_of_occurance(arr, k):
    low = 0
    high = len(arr)-1
    count = 0

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            count+=1
            
            low = mid-1
            while k == arr[low]:
                count += 1
                low-=1
                print("Enter 2nd while")
                print(count)
            
            high = mid+1
            while k == arr[high]:
                count += 1
                high+=1           
            return count
        
        elif k < arr[mid]:
            high = mid-1

        else:
            low = mid+1
        
    return 0
    
cnt = number_of_occurance(arr, target)
print(cnt)
