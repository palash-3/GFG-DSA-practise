nums = [1,2,3,4,4,3,2,1]

def array_shuffle(nums, n):
    result = []

    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    print(result)

array_shuffle(nums, 4)