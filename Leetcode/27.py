nums = [0,1,2,2,3,0,4,2]

def remove_element(nums, val):
    n = len(nums)
    k = 0

    for i in range(n):
        if nums[i] != val:
            if i != k:
                nums[k] = nums[i]
            k+=1
    return k

result = remove_element(nums, 2)
print(result)
            
