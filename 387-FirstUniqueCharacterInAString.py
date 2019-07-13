# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


class Solution(object):
    def firstUniqChar(self, s):
        freq_m = [0 for _ in range(26)]

        for ch in s:
            freq_m[ord(ch) - ord("a")] += 1
        for i in range(len(s)):
            if freq_m[ord(s[i]) - ord("a")] == 1:
                return i
        return -1
