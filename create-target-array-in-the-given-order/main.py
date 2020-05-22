def test(nums, index):
    target = []
    if not nums or not index:
        return target
    for i, num in zip(index, nums):
        target.insert(i, num)
    return target


def test2(nums, index):
    target = []
    if not nums or not index:
        return target
    for i, num in zip(index, nums):
        if i >= len(target):
            target.append(num)
        else:
            target = target[:i] + [num] + target[i:]

    return target


print(test([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))
print(test([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))

print()

print(test2([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))
print(test2([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
