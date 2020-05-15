def test(nums):
    global_sum = current_max = nums[0]
    for num in nums:
        current_max = max(num, current_max + num)
        global_sum = max(current_max, global_sum)
    return global_sum

# Kadane's Algorithm
# The idea is to calculate the previous best subarray and determining if the best subarray previous is better
# Than the current local number if it is then that is the best sub array if not, then the best subarray will
# Start from the local number and then (the following)

# [-2, 1, 3]
# [-2 ] is the current best (local)
# 1 (local) vs  (-2)current best + (1)local = since local is better than the combined previuos subarray then local becomes best
# 3 (local) vs (1) current best + (3) local = since current+local is better it becomes the current best
# Thus resulting in the best sum subarray  = 4 = [1,3]

test([-2, 1])
