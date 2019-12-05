# Given a string which consists of lowercase or uppercase letters, find the length of the
# longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_low = [0 for _ in range(26)]
        freq_up  = [0 for _ in range(26)]

        for i in range(len(s)):
            if ord(s[i]) >= ord("a") and ord(s[i]) <= ord("z"):
                freq_low[ord(s[i]) - ord("a")] += 1
            else:
                freq_up[ord(s[i]) - ord("A")] += 1

        res = 0
        spare = 0

        for i in range(len(freq_low)):
            res += freq_low[i] // 2
            res += freq_up[i] // 2
            if freq_low[i] % 2 != 0 or freq_up[i] % 2 != 0:
                spare = 1

        return res * 2 + spare
