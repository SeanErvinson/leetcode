def test(s):
    counter = 0
    result = 0
    for char in s:
        counter += 1 if char == "L" else -1
        if counter == 0:
            result += 1
    return result
    # r = 0
    # l = 0
    # result = 0
    # for char in s:
    #     if char == "L":
    #         l += 1
    #         r -= 1
    #     else:
    #         r += 1
    #         l -= 1
    #     if l == 0 and r == 0:
    #         result += 1
    # return result


print(test("RLLLLRRRLR"))  # 3
print(test("RLRRRLLRLL"))  # 2
print(test("LLLLRRRR"))  # 1
print(test("RLRRLLRLRL"))  # 4
