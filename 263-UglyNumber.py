# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True
        for f in [2, 3, 5]:
            if num % f == 0:
                if self.isUgly(int(num/f)):
                    return True
        return False
