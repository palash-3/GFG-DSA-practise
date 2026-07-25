nums = [1,1,0,1,1,1,0,0,0,0,0,0,0]

def max_consecutive_once(nums):
    cnt = 0
    max_cnt = 0

    for num in nums:
        if num == 0:
            cnt = 0
        else:
            cnt+=1
        max_cnt = max(max_cnt, cnt)
    return max_cnt

result = max_consecutive_once(nums)
print(result)

    


