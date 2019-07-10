# Given an integer, write a function to determine if it is a power of three.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (math.log10(n)/math.log10(3)).is_integer()
