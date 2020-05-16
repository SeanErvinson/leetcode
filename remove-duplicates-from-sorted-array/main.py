def test(nums):
    if not nums or len(nums) == 0:
        return 0
    current = nums[0]
    offset = 0
    for num in nums[1:]:
        if current > num:
            break
        if current == num:
            nums.remove(num)
            nums.append(num)
            offset += 1
        else:
            current = num
    return len(nums) - offset

    # if not nums:
    #     return
    # i = 1
    # n = nums[0]
    # for j in range(1, len(nums)):
    #     if nums[j] == n:
    #         continue
    #     else:
    #         n = nums[j]
    #         nums[i] = n
    #         i += 1
    # nums[:] = nums[:i]
    # return len(nums)

print(test([1, 1, 2]))
print(test([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(test([0]))
print(test([0, 2, 2, 2]))
