def test2(nums1, m, nums2, n):
    length_pointer = len(nums1) - 1
    while m and n:
        if nums1[m-1] > nums2[n-1]:
            nums1[length_pointer] = nums1[m-1]
            m -= 1
        else:
            nums1[length_pointer] = nums2[n-1]
            n -= 1
        length_pointer -= 1
    if n:
        nums1[:n] = nums2[:n]
    return nums1

def test(nums1, m, nums2, n):
    nums1 = nums1[:m]
    nums1.extend(nums2)
    nums1.sort()
    return nums1

print(test2([1], 1, [], 0))
print(test2([2, 0], 1, [1], 1))
print(test2([0], 0, [1], 1))
print(test2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(test2([1, 4, 7, 0, 0, 0], 3, [2, 3, 6], 3))


# print(test([1], 1, [], 0))
# print(test([2, 0], 1, [1], 1))
# print(test([0], 0, [1], 1))
# print(test([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
# print(test([1, 4, 7, 0, 0, 0], 3, [2, 3, 6], 3))
