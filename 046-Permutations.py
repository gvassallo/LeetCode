# Given a collection of distinct numbers, return all possible permutations.


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1: 
            return [nums]
        else: 
            result = [] 
            permutations = self.permute(nums[1::])
            for p in permutations: 
                for i in range(len(p) + 1): 
                    new_p = p[::]
                    new_p.insert(i, nums[0]) 
                    result.append(new_p)
            return result 


if __name__ == "__main__": 
    nums = [1, 2, 3]
    print Solution().permute(nums) 
