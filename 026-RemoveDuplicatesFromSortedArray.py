# Given a sorted array, remove the duplicates in-place such that each element appear only
# once and return the new length.  
# Do not allocate extra space for another array, you must do this by modifying the input
# array in-place with O(1) extra memory.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: 
            return 0 
        i = 0 
        for j in range(1, len(nums)): 
            if nums[j] > nums[i]: 
                i += 1
                nums[i] = nums[j] 
        return i + 1


if __name__ == "__main__": 
    nums = [1, 1, 2] 
    print Solution().removeDuplicates(nums) 
