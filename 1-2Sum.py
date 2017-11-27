# Given an array of integers, return indices of the two numbers such that they add up to a
# specific target.
# You may assume that each input would have exactly one solution, and you may not use the
# same element twice.
# Example: Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        chars = {} 
        for position in range(len(nums)): 
            chars[nums[position]] = position
        for i in range(len(nums)): 
            n = target - nums[i]
            if n in chars: 
                if i != chars[n]: 
                    return [i, chars[n]]
        return -1, -1              
       

if __name__ == "__main__": 
    nums = [2, 7, 11, 15] 
    print Solution().twoSum(nums, 9) 
