nums = [2,2,1,1,1,2,2]

def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count+=1
        else:
            count-=1

    count = 0
    for num in nums:
        if num == candidate:
            count+=1

    if count > (len(nums)//2):
        return candidate
    else:
        return -1

result = majority_element(nums)
print(result)