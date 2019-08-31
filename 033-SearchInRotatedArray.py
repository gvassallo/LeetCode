# Suppose an array sorted in ascending order is rotated at some pivot unknown to you
# beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index,
# otherwise return -1.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return self.helper(0, len(nums) - 1, nums, target)

    def helper(self, l, r, nums, target):
        if l > r:
            return -1
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= target <= nums[mid]:
                return self.helper(l, mid - 1, nums, target)
            else:
                return self.helper(mid + 1, r, nums, target)
        else:
            if nums[r] >= target >= nums[mid]:
                return self.helper(mid + 1, r, nums, target)
            else:
                return self.helper(l, mid - 1, nums, target)

if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    print Solution().search(nums, 0)
