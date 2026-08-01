nums = [1,1,1,2,2,3]

def remove_duplicate(nums):
    write_pos = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[write_pos - 2]:
            nums[write_pos] = nums[i]
            write_pos += 1
    return write_pos
result = remove_duplicate(nums)
print(result)


