def test(nums):
    pointer = 0
    for index, value in enumerate(nums):
        if value != 0:
            nums[index], nums[pointer] = nums[pointer], value
            pointer += 1


# def test(nums):
#     pointer = len(nums) - 1
#     for index, value in enumerate(nums):
#         if index >= pointer:
#             break
#         if value == 0:
#             for j in range(pointer, index, -1):
#                 pointer = min(pointer, j)
#                 if nums[j] != 0:
#                     value = nums[j] + value
#                     nums[j] = abs(nums[j] - value)
#                     nums[index] = abs(nums[j] - value)
#                     break
#             pointer -= 1

test([0, 1, 0, 0, 10, 12, 0])
