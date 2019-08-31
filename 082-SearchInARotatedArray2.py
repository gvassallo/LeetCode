# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true, otherwise return false.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return self.helper(0, len(nums) - 1, nums, target)

    def helper(self, l, r, nums, target):
        if l > r:
            return False
        mid = (l + r) // 2
        if nums[mid] == target:
            return True
        if nums[l] < nums[mid]:
            if nums[l] <= target <= nums[mid]:
                return self.helper(l, mid - 1, nums, target)
            else:
                return self.helper(mid + 1, r, nums, target)
        elif nums[l] > nums[mid]:
            if nums[r] >= target >= nums[mid]:
                return self.helper(mid + 1, r, nums, target)
            else:
                return self.helper(l, mid - 1, nums, target)
        else:
            if nums[mid] != nums[r]:
                return self.helper(mid + 1, r, nums, target)
            else:
                res = self.helper(mid + 1, r, nums, target)
                if res: return True
                return self.helper(l, mid - 1, nums, target)
