def helper(nums, l, r):
    if l == r:
        return nums[l]
    mid = (l + r) // 2
    left_max = helper(nums, l, mid)
    right_max = helper(nums, mid + 1, r)
    cross_max = cross_sum(nums, l, mid, r)
    return max(left_max, right_max, cross_max)


def cross_sum(nums, l, mid, r):
    left_sum = -float('inf')
    curr_sum = 0
    for i in range(mid, l - 1, -1):
        curr_sum += nums[i]
        left_sum = max(left_sum, curr_sum)
    right_sum = -float('inf')
    curr_sum = 0
    for i in range(mid + 1, r + 1):
        curr_sum += nums[i]
        right_sum = max(right_sum, curr_sum)
    return left_sum + right_sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return helper(nums, 0, len(nums) - 1)
