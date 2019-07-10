# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same character
# but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in mapping_s and t[i] not in mapping_t:
                mapping_s[s[i]] = t[i]
                mapping_t[t[i]] = s[i]
            elif mapping_t.get(t[i], "") != s[i] or mapping_s.get(s[i], "") != t[i]:
                    return False

        return True
