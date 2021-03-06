# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
#
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
#
# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        return self.helper(0, n)

    def helper(self, l, r):
        if l > r:
            return -1
        mid = (l + r) / 2
        res = guess(mid + 1)

        if res == 0:
            return mid + 1
        elif res == -1:
            return self.helper(l, mid - 1)
        else:
            return self.helper(mid + 1, r)
