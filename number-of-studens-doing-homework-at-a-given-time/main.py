def test(startTime, endTime, queryTime):
    result = 0
    for time1, time2 in zip(startTime, endTime):
        if time1 <= queryTime and queryTime <= time2:
            result += 1
    return result


print(test([1, 2, 3], [3, 2, 7], 4))  # 1
print(test([4], [4], 4))  # 1
print(test([4], [4], 5))  # 0
print(test([1, 1, 1, 1], [1, 3, 2, 4], 7))  # 0
print(test([9, 8, 7, 6, 5, 4, 3, 2, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10], 5))  # 5
