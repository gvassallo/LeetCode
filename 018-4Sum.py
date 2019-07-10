# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b +
# c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# Note: The solution set must not contain duplicate quadruplets.
# 
# Complexity O(N^3) 


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """ 
        res = []
        nums.sort() 
        for j in range(len(nums) - 3): 
            new_target = nums[j] - target 
            if j == 0 or (j > 0 and nums[j] != nums[j-1]): 
                for i in range(j + 1, len(nums)-2):  
                    if i == j + 1 or (i > j + 1 and nums[i] != nums[i - 1]):
                        lo = i + 1 
                        hi = len(nums) - 1
                        sum = -(new_target + nums[i])
                        while lo < hi:  
                            if nums[lo] + nums[hi] == sum: 
                                res.append([nums[j], nums[i], nums[lo], nums[hi]])
                                while lo < hi and nums[lo] == nums[lo + 1]: 
                                    lo += 1 
                                while lo < hi and nums[hi] == nums[hi - 1]: 
                                    hi -= 1 
                                lo += 1
                                hi -= 1
                            elif nums[lo] + nums[hi] < sum: 
                                lo += 1 
                            else: 
                                hi -= 1 
        return res


if __name__ == "__main__": 
    nums = [1, 0, -1, 0, -2, 2]
    print Solution().fourSum(nums, 0) 
