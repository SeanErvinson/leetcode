def test(nums):
    return sorted([num * num for num in nums])


print(test([-4, -1, 0, 3, 10]))
print(test([-7, -3, 2, 3, 11]))
