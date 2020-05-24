def test(nums):
    result = 0
    print(list(map(lambda num: not len(str(num)) % 2, nums)).count(True))
    for num in nums:
        if len(str(num)) % 2 == 0:
            result += 1
    return result


print(test([12, 345, 2, 6, 7896]))
print(test([12]))
print(test([]))
print(test([312331, 12312, 412, 412, 41, 241]))
