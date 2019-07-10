# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find
# all unique combinations in C where the candidate numbers sums to T.
# The same repeated number may be chosen from C unlimited number of times.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.


class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(target, index, partial):
            if target == 0: 
                result.append(partial)
                return 
            if target < 0: 
                return 
            for i in xrange(index, len(nums)): 
                helper(target - nums[i], i, partial + [nums[i]]) 
        nums.sort() 
        result = [] 
        helper(target, 0, []) 
        return result


if __name__ == "__main__": 
    nums = [2, 3, 6, 7]
    print Solution().combinationSum(nums, 7) 
