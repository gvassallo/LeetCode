# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that
# is missing from the array.

import math

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        bit_vector = 2**(len(nums)+1) - 1
        for x in nums:
            mask = ~(1 << x)
            bit_vector &= mask
        return int(math.log2(bit_vector))
