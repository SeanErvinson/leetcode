def test(nums, val):
    # print(len([nums[i] for i in range(len(nums)-1, -1, -1) if nums[i] != val])) # extra memory though
    for index in range(len(nums)-1, -1, -1):
        if nums[index] == val:
            del(nums[index])
    return len(nums)

print(test([0,1,2,2,3,0,4,2], 2))
print(test([3,2,2,3], 3))