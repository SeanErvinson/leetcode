def test(A):
    if len(A) < 3:
        return False
    # i = 0
    # while i < len(A) - 1 and A[i] < A[i + 1]:
    #     i += 1

    # if i == 0 or i == len(A) - 1:
    #     return False

    # while i < len(A) - 1:
    #     if A[i] <= A[i + 1]:
    #         return False
    #     i += 1
    # return True

    highest_point = A.index(max(A))
    left_section = A[:highest_point]
    right_section = A[highest_point:]
    if len(left_section) == 0 or len(right_section) == 1:
        return False
    current = left_section[0]
    for i in left_section[1:]:
        if current >= i:
            return False
        current = i
    current = right_section[0]
    for i in right_section[1:]:
        if current <= i:
            return False
        current = i
    return True


print(test([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # false
print(test([0, 1, 2, 3, 2, 1]))  # true
print(test([0, 3, 2, 1]))  # true
print(test([0, 1, 2, 1, 4, 5, 6, 3, 2, 1]))  # false
print(test([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  # false
print(test([3, 5, 5]))  # false
print(test([2, 1]))  # false
