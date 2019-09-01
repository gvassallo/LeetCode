# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -∞.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0 and (i == len(nums) - 1 or nums[i + 1] < nums[i]):
                return i
            if i == len(nums) - 1:
                return i
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i
