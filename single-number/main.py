def test(nums) -> int:
    for num in nums:
        if nums.count(num) == 1:
            return num


test([4,1,2,1,2])
