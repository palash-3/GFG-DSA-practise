nums = [0,0,1,1,1,2,2,3,3,4]

def remove_duplicate(nums:int)->int:
    n = len(nums)
    unique_idx = 0

    for i in range(n):
        if nums[i] != nums[unique_idx]:
            unique_idx+=1
            nums[unique_idx] = nums[i]
    return unique_idx+1

unique_val = remove_duplicate(nums)
print(unique_val)

