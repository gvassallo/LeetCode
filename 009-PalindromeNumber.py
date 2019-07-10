# Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        length = 1
        while (x / length) >= 10:
            length *= 10

        while x != 0:
            left = x // length
            right = x % 10

            if left != right:
                return False

            x = (x % length) // 10
            length /= 100
        return True
