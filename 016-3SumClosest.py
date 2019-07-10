# Given an array S of n integers, find three integers in S such that the sum is closest to
# a given number, target. Return the sum of the three integers. You may assume that each
# input would have exactly one solution.
# 
# Complexity O(N^2) 


import sys 


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort() 
        min_diff = sys.maxsize
        closest_sum = 0 
        for i in range(len(nums) - 2):  
            lo = i + 1 
            hi = len(nums) - 1 
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < min_diff: 
                    min_diff = abs(target - sum) 
                    closest_sum = sum 
                if closest_sum <= target: 
                    lo += 1 
                if closest_sum > target: 
                    hi -= 1 
        return closest_sum


if __name__ == "__main__": 
    nums = [-1, 2, 1, -4]
    print Solution().threeSumClosest(nums, 1) 
