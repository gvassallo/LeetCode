# Given two strings s and t which consist of only lowercase letters.
#
# String t is generated by random shuffling string s and then add one more letter at a random position.
#
# Find the letter that was added in t.

import math

class Solution(object):
    def findTheDifference(self, s: str, t: str) -> str:
        bit_vector = 0

        for i in range(len(t)):
            if i < len(s):
                mask = 1 << ord(s[i]) - ord("a")
                bit_vector ^= mask
            mask = 1 << ord(t[i]) - ord("a")
            bit_vector ^= mask
        return chr(int(math.log2(bit_vector)) + ord("a"))
