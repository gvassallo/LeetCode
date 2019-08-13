# Given a collection of integers that might contain duplicates, nums,
# return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(sorted(nums), 0, [], res)
        return res

    def helper(self, nums, index, part, res):
        res.append(part)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i -1]:
                continue
            self.helper(nums, i + 1, part + [nums[i]], res)
