# Given an array nums, write a function to move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
            else:
                nums[i - zeroes] = nums[i]
        for i in range(len(nums) - zeroes, len(nums)):
            nums[i] = 0
