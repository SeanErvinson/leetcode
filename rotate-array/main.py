def test(nums, k):
    rotation = k % len(nums)
    for _ in range(rotation):
        nums.insert(0, nums[-1])
        nums.pop()
    return nums


def test2(nums, k):
    k %= len(nums)

    def reverse(nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    # Assuming [1,2,3,4,5] k = 2

    # 5 2 3 4 1
    # 5 2 3 4 1
    # 5 4 3 2 1
    reverse(nums, 0, len(nums) - 1)  # Reverse full
    # 3 4 5 2 1
    reverse(nums, 0, k - 1)  # Reverse left
    # 3 4 5 1 2
    reverse(nums, k, len(nums) - 1)  # Reverse right


print(test2([1, 2, 3, 4, 5], 3))
print(test2([1, 2, 3, 4, 5, 6, 7], 3))
print(test2([-1, -100, 3, 99], 2))

