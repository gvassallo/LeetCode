# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        freq = [0 for _ in range(26)]
        result = []
        for i in range(len(p)):
            freq[ord(p[i]) - ord('a')] += 1
            if i < len(p) - 1:
                freq[ord(s[i]) - ord('a')] -= 1
        j = 0
        for i in range(len(p) - 1, len(s)):
            freq[ord(s[i]) - ord('a')] -= 1
            if all(v == 0 for v in freq):
                result.append(j)
            freq[ord(s[j]) - ord('a')] += 1
            j += 1

        return result
