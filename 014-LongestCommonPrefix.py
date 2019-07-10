# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        min_len = min(map(lambda x: len(x), strs))
        max_index = self.find_max_index(strs, min_len)
        return strs[0][:max_index]

    def find_max_index(self, strs, min_len):
        for i in range(min_len):
            ch = strs[0][i]
            for s in strs[1:]:
                if s[i] != ch:
                    return i
        return min_len
