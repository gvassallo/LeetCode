# Find the contiguous subarray within an array (containing at least one number) which has
# the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            if curr >= 0: 
                curr += nums[i]
            else: 
                curr = nums[i]
            if curr > max: 
                max = curr 
        return max 


if __name__ == "__main__": 
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print Solution().maxSubArray(nums)
