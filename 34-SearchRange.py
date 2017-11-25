# Given an array of integers sorted in ascending order, find the starting and ending
# position of a given target value.  
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
# For example, Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4] 


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) / 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]


if __name__ == "__main__": 
    nums = [5, 7, 7, 8, 8, 10]
    print Solution().searchRange(nums, 8) 
