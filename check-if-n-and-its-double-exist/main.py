def test(arr):
    previous_nums = set()
    for index, value in enumerate(arr):
        double_num = value * 2
        if double_num in arr[index + 1 :] or double_num in previous_nums:
            return True
        previous_nums.add(value)
    return False


print(test([10, 2, 5, 3]))  # true
print(test([-2, 0, 10, -19, 4, 6, -8]))  # false
print(test([7, 1, 14, 11]))  # true
print(test([0, 0]))  # true
print(test([3, 1, 7, 11]))  # false
