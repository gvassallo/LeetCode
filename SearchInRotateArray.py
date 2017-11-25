# Suppose an array sorted in ascending order is rotated at some pivot unknown to you 
# beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index, 
# otherwise return -1.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_helper(nums, target, 0, len(nums)-1) 
        
    def search_helper(self, nums, target, left, right):
        if left > right: return -1 
        mid = (left + right) / 2 
        if nums[mid] == target: 
            return mid 
        if nums[left] < nums[mid]: 
            if target >= nums[left] and target < nums[mid]: 
                return self.search_helper(nums, target, left, mid - 1)
            else: 
                return self.search_helper(nums, target, mid + 1, right)
        elif nums[left] > nums[mid]: 
            if target > nums[mid] and target <= nums[right]: 
                return self.search_helper(nums, target, mid + 1, right)
            else: 
                return self.search_helper(nums, target, left, mid - 1)
        elif nums[left] == nums[mid]: 
            if nums[mid] != nums[right]: 
                return self.search_helper(nums, target, mid + 1, right)
            else: 
                res = self.search_helper(nums, target, left, mid - 1)
                if res == -1: 
                    return self.search_helper(nums, target, mid + 1, right)
                else: 
                    return res 
        return -1 


if __name__ == "__main__": 
    nums = [4, 5, 6, 7, 0, 1, 2]
    print Solution().search(nums, 0) 

