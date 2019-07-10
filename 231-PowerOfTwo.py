# Given an integer, write a function to determine if it is a power of two.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        ones = 0
        while n != 0:
            if n & 1:
                ones += 1
            n = n >> 1
        return ones == 1
