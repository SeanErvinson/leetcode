def test(nums):
    highest = 0
    current_one = 0
    for num in nums:
        if num == 1:
            current_one += 1
            if current_one > highest:
                highest = current_one
        else:
            current_one = 0
    return highest


print(test([1, 1, 0, 1, 1, 1]))
print(test([1, 0, 1, 1, 0, 1]))
print(test([0, 1]))
