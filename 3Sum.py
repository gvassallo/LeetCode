# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Note: The solution set must not contain duplicate triplets.
# 
# Complexity O(N^2) 


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort() 
        for i in range(len(nums)-2): 
            if i == 0 or (i > 0 and nums[i] != nums[i-1]): 
                lo = i + 1 
                hi = len(nums) - 1
                s = -nums[i]
                while lo < hi:  
                    if nums[lo] + nums[hi] == s: 
                        res.append([nums[i], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo + 1]: 
                            lo += 1 
                        while lo < hi and nums[hi] == nums[hi - 1]: 
                            hi -= 1 
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < s: 
                        lo += 1 
                    else: 
                        hi -= 1 
        return res


if __name__ == "main": 
    nums = [-1, 0, 1, 2, -1, -4]
    print Solution().threeSum(nums) 
