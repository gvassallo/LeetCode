# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        i = len(nums) - 1
        j = i - 1
        while j >= 0:
            if nums[j] >= (i - j):
                i = j
                j -= 1
            else:
                j -= 1
        return nums[0] >= i
