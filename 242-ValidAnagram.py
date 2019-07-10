# Given two strings s and t , write a function to determine if t is an anagram of s.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = [0 for _ in range(26)]
        freq_t = [0 for _ in range(26)]

        for i in range(len(s)):
            ch = ord(s[i]) - ord('a')
            freq_s[ch] += 1
            ch = ord(t[i]) - ord('a')
            freq_t[ch] += 1

        for i in range(26):
            if freq_s[i] != freq_t[i]:
                return False

        return True
